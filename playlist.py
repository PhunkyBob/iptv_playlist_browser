# -*- coding: utf-8 -*-
"""
This class manage the conversion of a playlist or Xtream credentials to groups / categories / channels.
"""

import os
import re
import requests
import json
import base64
from typing import Tuple, Set, List, Dict
from collections import defaultdict


"""
Xtream API
# Account
{server}/player_api.php?username={username}&password={password}

# Live categories
{server}/player_api.php?username={username}&password={password}&action=get_live_categories
# Live streams
{server}/player_api.php?username={username}&password={password}&action=get_live_streams
# EPG
{server}/player_api.php?username={username}&password={password}&action=get_simple_data_table&stream_id=53375

# VOD categories
{server}/player_api.php?username={username}&password={password}&action=get_vod_categories
# VOD streams
{server}/player_api.php?username={username}&password={password}&action=get_vod_streams
# Serie infos
{server}/player_api.php?username={username}&password={password}&action=get_vod_info&vod_id=X

# Series categories
{server}/player_api.php?username={username}&password={password}&action=get_series_categories
# Series streams
{server}/player_api.php?username={username}&password={password}&action=get_series
# Serie infos
{server}/player_api.php?username={username}&password={password}&action=get_series_info&series_id=X

"""


class Playlist:
    channels: Dict = {}
    channels_details: Dict = {}
    channels_epg: Dict = {}
    vod: Dict = {}
    vod_details: Dict = {}
    series: Dict = {}
    series_details: Dict = {}
    api_account: Dict = {}
    temp_folder: str = "temp"
    default_category: str = "OTHERS"

    def __init__(
        self,
        server: str = "",
        username: str = "",
        password: str = "",
        filename: str = "",
        try_xtream: bool = True,
        sep_lvl1: str = "▼---",
        sep_lvl2: str = "---●★",
    ) -> None:
        if filename:
            # If the file is remote, download it
            if filename.lower().startswith("http"):
                filename = self.download_remote_file(filename)
                if not filename:
                    return

            if not os.path.isfile(filename):
                print(f'[ERROR] File "{filename}" is unavailable...')
                return

            server, username, password = Playlist.get_credentials_from_file(filename)
            # Even if it's a playlist, we try to get Xtream credentials
            if (
                try_xtream
                and server
                and self.load_from_api(
                    server,
                    username,
                    password,
                    sep_lvl1=sep_lvl1,
                    sep_lvl2=sep_lvl2,
                )
            ):
                return
            # Load from a file
            return self.load_from_file(filename, sep_lvl1, sep_lvl2)

        if server:
            # Load from API
            self.load_from_api(server, username, password, sep_lvl1=sep_lvl1, sep_lvl2=sep_lvl2)
            return

    def download_remote_file(self, url: str) -> str:
        response = requests.get(url)
        if response.status_code not in {200, 201}:
            print("[ERROR] Can't download file")
            return False

        os.makedirs(f"{self.temp_folder}", exist_ok=True)
        tmp_filename = "temp.m3u"
        if "Content-Disposition" in response.headers:
            if res := re.search(r"filename=\"(.+?)\"", response.headers["Content-Disposition"]):
                if res[1]:
                    tmp_filename = res[1]

        cached_file = f"{self.temp_folder}/{tmp_filename}"
        with open(cached_file, "wb") as pl:
            pl.write(response.content)
        return cached_file

    @staticmethod
    def get_api_infos(server: str, username: str, password: str) -> Dict:
        # Connect to the API and get global infos
        res = requests.get(f"{server}/player_api.php?username={username}&password={password}")
        if res.status_code not in {200, 201}:
            print("[ERROR] Bad credentials...")
            return False
        return json.loads(res.text)

    def load_from_api(
        self, server: str, username: str, password: str, sep_lvl1: str = "", sep_lvl2: str = "---"
    ) -> bool:
        """Create a playlist from Xtream credentials."""
        try:
            # Connect to the API and get global infos
            self.api_account = Playlist.get_api_infos(server, username, password) or {}
            if not self.api_account:
                return False

            # Get channels
            self.channels, self.channels_details = Playlist.load_streams(
                server, username, password, "live", sep_lvl1, sep_lvl2, self.default_category
            )

            # Get movies
            self.vod, self.vod_details = Playlist.load_streams(server, username, password, "vod", sep_lvl1, sep_lvl2)

            # Get series
            self.series, self.series_details = Playlist.load_streams(
                server, username, password, "series", sep_lvl1, sep_lvl2
            )
        except Exception:
            return False
        return True

    @staticmethod
    def get_categories(server: str, username: str, password: str, category_type: str = "live") -> Dict:
        try:
            res = requests.get(
                f"{server}/player_api.php?username={username}&password={password}&action=get_{category_type}_categories"
            )
        except Exception:
            return False
        if res.status_code not in {200, 201}:
            print("[ERROR] Bad credentials...")
            return False
        categories = json.loads(res.text)
        return defaultdict(lambda: "OTHERS", {c["category_id"]: c["category_name"] for c in categories})

    @staticmethod
    def get_streams(server: str, username: str, password: str, category_type: str = "live") -> Dict:
        stream_txt = "_streams" if category_type in {"live", "vod"} else ""
        try:
            res = requests.get(
                f"{server}/player_api.php?username={username}&password={password}&action=get_{category_type}{stream_txt}"
            )
        except Exception:
            return False
        if res.status_code not in {200, 201}:
            print("[ERROR] Bad credentials...")
            return False
        return json.loads(res.text)

    @staticmethod
    def load_streams(
        server: str,
        username: str,
        password: str,
        category_type: str = "live",
        sep_lvl1: str = "",
        sep_lvl2: str = "---",
        default_category: str = "OTHERS",
    ) -> Tuple[Dict, Dict]:
        current_lvl1: str = ""
        current_lvl1_previous: str = ""
        current_lvl2: str = ""
        urls_details: Dict = {}
        categories: Dict = Playlist.get_categories(server, username, password, category_type)
        if categories == False:
            return False
        # Exemple: ['category lvl 1']['category lvl 2']['channel name'] = 'http://...'
        urls = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {})))
        live_streams = Playlist.get_streams(server, username, password, category_type)
        if live_streams == False:
            return False
        for s in live_streams:
            sub_folder = {"live": "", "vod": "/movie", "series": "/series"}[category_type]
            if "stream_id" in s:
                ext = "." + s["container_extension"] if "container_extension" in s else ""
                url = f"{server}{sub_folder}/{username}/{password}/{s['stream_id']}{ext}"
            else:
                url = s["series_id"]
            # Decide what category we're in
            current_lvl1 = categories[s["category_id"]]
            if current_lvl1 != current_lvl1_previous:
                current_lvl2 = default_category
            title = Playlist.clean_title(s["name"])
            if sep_lvl1 and sep_lvl1 in title:
                continue
            if sep_lvl2 and sep_lvl2 in title:
                current_lvl2 = title
                current_lvl1_previous = current_lvl1
                continue
            urls[current_lvl1][current_lvl2][title] = url
            # Save details for later (EPG).
            urls_details[url]: Dict = {
                key: s[key]
                for key in {
                    "is_adult",
                    "name",
                    "stream_type",
                    "rating",
                    "epg_channel_id",
                    "tv_archive",
                    "tv_archive_duration",
                    "stream_icon",
                    "stream_id",
                    "direct_source",
                }
                if key in s
            }
            current_lvl1_previous = current_lvl1
        return urls, urls_details

    def get_series(self, series_id):
        if not self.api_account:
            return
        server = (
            self.api_account["server_info"]["server_protocol"]
            + "://"
            + self.api_account["server_info"]["url"]
            + ":"
            + self.api_account["server_info"]["port"]
        )
        username = self.api_account["user_info"]["username"]
        password = self.api_account["user_info"]["password"]
        res = requests.get(
            f"{server}/player_api.php?username={username}&password={password}&action=get_series_info&series_id={series_id}"
        )
        if res.status_code not in {200, 201}:
            print("[ERROR] Bad credentials...")
            return False
        series = json.loads(res.text)
        urls = {}
        for season in series["episodes"]:
            for episode in series["episodes"][season]:
                title = Playlist.clean_title(episode["title"])
                url = f"{server}/series/{username}/{password}/{episode['id']}.{episode['container_extension']}"
                urls[title] = url
        return urls

    def load_from_file(self, filename: str, sep_lvl1: str = "▼---", sep_lvl2: str = "---●★"):
        """Create a playlist from a m3u file."""
        # Content exemple for urls:
        # urls['channels']['category lvl 1']['category lvl 2']['channel name'] = "http://channel_url"
        urls: Dict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {})))
        current_lvl1: Dict = defaultdict(lambda: self.default_category)
        current_lvl2: Dict = defaultdict(lambda: self.default_category)

        # TODO: load each line as CSV because the "," in a title could create problems.
        with open(filename, "r", encoding="utf-8") as f:
            while content := f.readline():
                content = content.strip()
                # content = normalize("NFKD", content)
                if not content.startswith("#EXTINF:-1"):
                    continue
                title = ",".join(content.split(",")[1:])
                title = Playlist.clean_title(title)

                group_title = ""
                subgroup_title = ""
                if res := re.search(r"group-title=\"(.+)\"", content):
                    group_title = res[1]
                    subgroup_title = self.default_category
                url = f.readline().strip()

                url_type = "channels"
                if re.match(r"http(.+)/movie/", url):
                    url_type = "movies"
                if re.match(r"http(.+)/series/", url):
                    url_type = "series"

                # Decide what category we're in
                if sep_lvl1 and sep_lvl1 in title:
                    current_lvl1[url_type] = title
                    continue
                if sep_lvl2 and sep_lvl2 in title:
                    current_lvl2[url_type] = title
                    continue

                # Test if is movie
                if url_type == "movies":
                    # TODO: later
                    continue
                # Test if is serie
                if url_type == "series":
                    # TODO: later
                    continue

                urls[url_type][group_title or current_lvl1[url_type]][subgroup_title or current_lvl2[url_type]][
                    title
                ] = url
        self.channels = urls["channels"]
        self.vod = urls["movies"]
        self.series = urls["series"]
        return True

    def update_epg(self, stream):
        """Call API to get the EPG for a stream."""
        server = self.api_account["server_info"]["url"]
        protocol = self.api_account["server_info"]["server_protocol"]
        port = self.api_account["server_info"]["port"]
        username = self.api_account["user_info"]["username"]
        password = self.api_account["user_info"]["password"]
        url = f"{protocol}://{server}:{port}/player_api.php?username={username}&password={password}&action=get_simple_data_table&stream_id={stream}"
        res = requests.get(url)
        if res.status_code not in {200, 201}:
            print("[ERROR] Bad credentials...")
            return False

        self.channels_epg[stream] = {}
        res = json.loads(res.text)
        if "epg_listings" not in res:
            return False
        for elem in res["epg_listings"]:
            if elem["has_archive"] or elem["now_playing"]:
                title = Playlist.clean_title(Playlist.decode(elem["title"]))
                description = Playlist.decode(elem["description"])
                start_timestamp = int(elem["start_timestamp"])
                stop_timestamp = int(elem["stop_timestamp"])
                res = re.search("(\d\d\d\d-\d\d-\d\d) (\d\d:\d\d):\d\d", elem["start"])
                start_date = res[1]
                start_time = res[2]
                duration = int((stop_timestamp - start_timestamp) / 60)
                epg = {
                    "title": title,
                    "description": description,
                    "start_date": start_date,
                    "start_time": start_time,
                    "duration": duration,
                }
                epg_id = f"[{start_date} {start_time}] {title} ({duration} min)"
                self.channels_epg[stream][epg_id] = epg

    @staticmethod
    def get_credentials_from_file(filename: str) -> Tuple[str, str, str]:
        server: str = ""
        username: str = ""
        password: str = ""
        with open(filename, "r", encoding="utf-8") as f:
            while content := f.readline():
                if res := re.search(r"^http(s?)://(.+)/(.+)/(.+)/([\d]+)$", content.strip(), re.IGNORECASE):
                    server = f"http{res[1]}://{res[2]}"
                    username = res[3]
                    password = res[4]
                    break
        return server, username, password

    @staticmethod
    def decode(base64_string):
        """Decode strings from the EPG."""
        base64_bytes = base64_string.encode("utf-8")
        result_string_bytes = base64.b64decode(base64_bytes)
        return result_string_bytes.decode("utf-8")

    @staticmethod
    def clean_title(title):
        title = title.strip()
        title = title.replace("&amp;", "&")
        return title


if __name__ == "__main__":
    Playlist(filename="tv_channels.m3u")
