import sys
import os
import configparser
from typing import Tuple, Dict

sys.path.append("..")
from playlist import Playlist

TEST_PLAYLIST = "tests/resources/test_playlist.m3u"
CONFIG_FILE = "tests/config.ini"


def _get_credentials_from_config():
    config = configparser.ConfigParser()
    if not os.path.isfile(CONFIG_FILE):
        print("WARNING: can't find config file")
        print("WARNING: xtream code won't be tested")
        return
    config.read(CONFIG_FILE, encoding="utf-8")
    return {
        "username": config["XTREAM_CODE"]["username"],
        "password": config["XTREAM_CODE"]["password"],
        "server": config["XTREAM_CODE"]["server"],
    }


def test_get_credentials_from_file():
    server, username, password = Playlist.get_credentials_from_file(TEST_PLAYLIST)
    assert server == "http://myserver.com:8000"
    assert username == "login"
    assert password == "password"


def test_download_remote_file():
    pass


def test_load_from_file():
    pl = Playlist()
    pl.load_from_file(TEST_PLAYLIST)
    assert len(pl.channels) == 3
    _check_channels_categories(pl, "▼---Main group 1---▼", "---●★Sub group 1★●---", "Channel 1")
    assert len(pl.channels["▼---Main group 1---▼"]["---●★Sub group 1★●---"]) == 2
    assert (
        pl.channels["▼---Main group 1---▼"]["---●★Sub group 1★●---"]["Channel 1"]
        == "http://myserver.com:8000/login/password/1"
    )
    _check_channels_categories(pl, "Specific group", "OTHERS", "Channel 3")


def _check_channels_categories(pl, arg0, arg2, arg3):
    assert arg0 in pl.channels
    assert arg2 in pl.channels[arg0]
    assert arg3 in pl.channels[arg0][arg2]


def test_get_api_infos():
    conf = _get_credentials_from_config()
    api_account = Playlist.get_api_infos(conf["server"], conf["username"], conf["password"])
    assert api_account["user_info"]["username"] == conf["username"]


def test_get_categories():
    conf = _get_credentials_from_config()
    categories = Playlist.get_categories(conf["server"], conf["username"], conf["password"])
    assert len(categories) > 0


def test_get_streams():
    conf = _get_credentials_from_config()
    streams = Playlist.get_streams(conf["server"], conf["username"], conf["password"])
    assert len(streams) > 0


def test_load_from_api():
    conf = _get_credentials_from_config()
    pl = Playlist()
    assert pl.load_from_api(conf["server"], conf["username"], conf["password"])


def test_load_streams_error():
    pl = Playlist()
    assert pl.load_streams("https://unexisting-xtream-code-provider.com", "foo", "bar") == False


def test_load_streams():
    conf = _get_credentials_from_config()
    pl = Playlist()
    urls, urls_details = pl.load_streams(conf["server"], conf["username"], conf["password"])
    assert len(urls) > 0
    assert len(urls_details) > 0


def test_download_m3u():
    conf = _get_credentials_from_config()
    pl = Playlist()
    file = pl.download_m3u(conf["server"], conf["username"], conf["password"], "tests")
    assert os.path.exists(file)
    assert os.path.getsize(file) > 0


def test_download_m3u_error():
    pl = Playlist()
    file = pl.download_m3u("https://unexisting-xtream-code-provider.com", "foo", "bar", "tests")
    assert file == False


def test_generate_m3u():
    pl = Playlist()
    pl.load_from_file(TEST_PLAYLIST)
    file = "tests/generated_playlist.m3u"
    pl.generate_m3u(file, export_live=True)
    assert os.path.exists(file)
    assert os.path.getsize(file) > 0


def test_generate_m3u_full():
    conf = _get_credentials_from_config()
    pl = Playlist()
    pl.load_from_api(conf["server"], conf["username"], conf["password"])
    file = "tests/generated_playlist.m3u"
    pl.generate_m3u(file, export_live=True, export_vod=True, export_series=True)
    assert os.path.exists(file)
    assert os.path.getsize(file) > 0


def test_decode():
    assert Playlist.decode("TcOpdMOpbw==") == "Météo"


def test_clean_title():
    assert Playlist.clean_title("  Foo &amp; bar  ") == "Foo & bar"


if __name__ == "__main__":
    print("Tests")
