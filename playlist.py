# -*- coding: utf-8 -*-
"""
This class manage the conversion of a playlist or Xtream credentials to groups / categories / channels.
"""

import base64
import json
import os
import re

import requests
import requests_random_user_agent  # noqa

"""
Xtream API

# M3u8 playlist
{server}/get.php?username={username}&password={password}&type=m3u_plus&output=m3u8

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
    channels = {}
    channels_details = {}
    channels_epg = {}
    image_urls = {}
    vod = {}
    vod_details = {}
    series = {}
    series_details = {}
    api_account = {}
    temp_folder = "temp"
    default_category: str = "OTHERS"

    def __init__(
            self, server="", username="", password="", filename="", try_xtream=True, sep_lvl1="▼---", sep_lvl2="---●★"
    ) -> None:
        if filename:
            # If the file is remote, download it
            filename = self.remote_download(filename)

            if not os.path.isfile(filename):
                print(f'[ERROR] File "{filename}" is unavailable...')

            if try_xtream:
                # Even if it's a playlist, we try to get Xtream credentials
                with open(filename, "r", encoding="utf-8") as f:
                    while content := f.readline():
                        if res := re.search(r"^http(s?)://(.+)/(.+)/(.+)/(\d+)$", content.strip(), re.IGNORECASE):
                            server = f"http{res[1]}://{res[2]}"
                            username = res[3]
                            password = res[4]
                            if self.load_from_api(server, username, password, sep_lvl1=sep_lvl1, sep_lvl2=sep_lvl2):
                                return
                            break

            # Load from a file
            self.load_from_file(filename, sep_lvl1, sep_lvl2)
            return

        # Load from API
        self.load_from_api(server, username, password, sep_lvl1=sep_lvl1, sep_lvl2=sep_lvl2)
        return

    def remote_download(self, filename):
        if filename.lower().startswith("http"):
            response = requests.get(filename)
            if not response.ok:
                print("[ERROR] Can't download file")

            os.makedirs(f"{self.temp_folder}", exist_ok=True)
            tmp_filename = "temp.m3u"
            if "Content-Disposition" in response.headers:
                if res := re.search(r"filename=\"(.+?)\"", response.headers["Content-Disposition"]):
                    if res[1]:
                        tmp_filename = res[1]

            cached_file = f"{self.temp_folder}/{tmp_filename}"
            with open(cached_file, "wb") as pl:
                pl.write(response.content)
            filename = cached_file
        return filename

    def load_from_api(self, server, username, password, sep_lvl1="", sep_lvl2="---"):
        """Create a playlist from Xtream credentials."""
        try:
            # Connect to the API and get global infos
            res = requests.get(f"{server}/player_api.php?username={username}&password={password}")
            if not res.ok:
                print("[ERROR] Bad credentials...")
                return False
            self.api_account = json.loads(res.text)

            # Get channels
            self.channels, self.channels_details = self.load_streams(
                server, username, password, "live", sep_lvl1, sep_lvl2
            )

            # Get movies
            self.vod, self.vod_details = self.load_streams(server, username, password, "vod", sep_lvl1, sep_lvl2)

            # Get series
            self.series, self.series_details = self.load_streams(
                server, username, password, "series", sep_lvl1, sep_lvl2
            )

        except Exception:
            return False

        return True

    def export_m3u8(self, server, username, password):
        """Export the playlist in M3U8 format."""
        get_m3u8 = requests.get(
            f"{server}/get.php?username={username}&password={password}&type=m3u_plus", stream=True
        )
        if get_m3u8.ok:
            return get_m3u8.raw
        print("[ERROR] Bad credentials or closed endpoint for xstream-codes...")
        return False

    def load_streams(self, server, username, password, type=None, sep_lvl1="", sep_lvl2="---"):
        current_lvl1_previous = ""
        current_lvl2 = ""
        urls_details = {}
        res = requests.get(
            f"{server}/player_api.php?username={username}&password={password}&action=get_{type}_categories"
        )
        if not res.ok:
            print("[ERROR] Bad credentials...")
            return False
        live_categories = json.loads(res.text)
        categories = {c["category_id"]: c["category_name"] for c in live_categories}
        urls = {c["category_name"]: {} for c in live_categories}
        stream_txt = "_streams" if type in ("live", "vod") else ""
        res = requests.get(
            f"{server}/player_api.php?username={username}&password={password}&action=get_{type}{stream_txt}"
        )
        if not res.ok:
            print("[ERROR] Bad credentials...")
            return False
        live_streams = json.loads(res.text)
        for s in live_streams:
            sub_folder = {"live": "", "vod": "/movie", "series": "/series"}[type]
            if "stream_id" in s:
                ext = "." + s["container_extension"] if "container_extension" in s else ""
                url = f"{server}{sub_folder}/{username}/{password}/{s['stream_id']}{ext}"
            else:
                url = s["series_id"]
            # Decide what category we're in
            if s["category_id"] not in categories:
                categories[s["category_id"]] = "OTHERS"
                if "OTHERS" not in urls:
                    urls["OTHERS"] = {}
            current_lvl1 = categories[s["category_id"]]
            if current_lvl1 != current_lvl1_previous:
                current_lvl2 = self.default_category
                if current_lvl2 not in urls[current_lvl1]:
                    urls[current_lvl1][current_lvl2] = {}
            title = self.clean_title(s["name"])
            if sep_lvl1 and sep_lvl1 in title:
                continue
            if sep_lvl2 and sep_lvl2 in title:
                current_lvl2 = title
                if current_lvl2 not in urls[current_lvl1]:
                    urls[current_lvl1][current_lvl2] = {}
                current_lvl1_previous = current_lvl1
                continue
            urls[current_lvl1][current_lvl2][title] = url
            # Save details for later (EPG).
            urls_details[url] = {}
            for key in (
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
            ):
                if key in s:
                    urls_details[url][key] = s[key]
            current_lvl1_previous = current_lvl1
        return urls, urls_details

    def get_series(self, series_id):
        if self.api_account:
            server = (
                f"""{self.api_account["server_info"]["server_protocol"]}://{self.api_account["server_info"]["url"]}:{self.api_account["server_info"]["port"]}""")
            username = self.api_account["user_info"]["username"]
            password = self.api_account["user_info"]["password"]
            res = requests.get(
                f"{server}/player_api.php?username={username}&password={password}&action=get_series_info&series_id={series_id}"
            )
            if not res.ok:
                print("[ERROR] Bad credentials...")
                return False
            series = json.loads(res.text)
            urls = {}
            for season in series["episodes"]:
                for episode in series["episodes"][season]:
                    title = self.clean_title(episode["title"])
                    url = f"{server}/series/{username}/{password}/{episode['id']}.{episode['container_extension']}"
                    urls[title] = url
            return urls

    def load_from_file(self, filename, sep_lvl1="▼---", sep_lvl2="---●★"):
        """Create a playlist from a m3u file."""
        urls = {"channels": {}, "movies": {}, "series": {}}
        current_lvl1 = {
            "channels": self.default_category,
            "movies": self.default_category,
            "series": self.default_category,
        }
        current_lvl2 = {
            "channels": self.default_category,
            "movies": self.default_category,
            "series": self.default_category,
        }

        # TODO: load each line as CSV because the "," in a title could create problems.
        with open(filename, "r", encoding="utf-8") as f:
            while content := f.readline():
                content = content.strip()
                # content = normalize("NFKD", content)
                if not content.startswith("#EXTINF:-1"):
                    continue
                title = ",".join(content.split(",")[1:])
                title = self.clean_title(title)

                group_title = ""
                if res := re.search(r"group-title=\"(.+)\"", content):
                    group_title = res[1]
                url = f.readline().strip()

                url_type = "channels"
                if re.match(r"http(.+)/movie/", url):
                    url_type = "movies"
                if re.match(r"http(.+)/series/", url):
                    url_type = "series"

                # Decide what category we're in
                if sep_lvl1 and sep_lvl1 in title:
                    current_lvl1[url_type] = group_title or title
                    current_lvl2[url_type] = self.default_category
                    continue
                if sep_lvl2 and sep_lvl2 in title:
                    current_lvl2[url_type] = title
                    continue

                # Test if is movie
                if url_type == "movies":
                    continue
                # Test if is serie
                if url_type == "series":
                    # TODO: later
                    continue

                if current_lvl1[url_type] not in urls[url_type]:
                    urls[url_type][current_lvl1[url_type]] = {}
                if current_lvl2[url_type] not in urls[url_type][current_lvl1[url_type]]:
                    urls[url_type][current_lvl1[url_type]][current_lvl2[url_type]] = {}
                urls[url_type][current_lvl1[url_type]][current_lvl2[url_type]][title] = url
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
        if not res.ok:
            print("[ERROR] Bad credentials...")
            return False

        self.channels_epg[stream] = {}
        res = json.loads(res.text)
        if "epg_listings" not in res:
            return False
        for elem in res["epg_listings"]:
            if elem["has_archive"] or elem["now_playing"]:
                title = self.clean_title(self.decode(elem["title"]))
                description = self.decode(elem["description"])
                start_timestamp = int(elem["start_timestamp"])
                stop_timestamp = int(elem["stop_timestamp"])
                res = re.search("(\d\d\d\d-\d\d-\d\d) (\d\d:\d\d):\d\d", elem["start"])
                start_date = res[1]
                start_time = res[2]
                duration = int((stop_timestamp - start_timestamp) / 60)
                epg = {
                    "title": title, "description": description, "start_date": start_date, "start_time": start_time,
                    "duration": duration
                }

                _id = f"[{start_date} {start_time}] {title} ({duration} min)"
                self.channels_epg[stream][_id] = epg

    def decode(self, base64_string):
        """Decode strings from the EPG."""
        base64_bytes = base64_string.encode("utf-8")
        result_string_bytes = base64.b64decode(base64_bytes)
        return result_string_bytes.decode("utf-8")

    def clean_title(self, title):
        title = title.strip()
        title = title.replace("&amp;", "&")
        return title


if __name__ == "__main__":
    Playlist(filename="tv_channels.m3u")
