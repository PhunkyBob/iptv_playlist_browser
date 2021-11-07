# -*- coding: utf-8 -*-
"""
This class allows to display the main application window.
"""

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from main_ui import Ui_MainWindow
from PyQt5.uic import loadUi
from playlist import Playlist
import subprocess
import psutil
from PyQt5 import QtCore, QtGui
from datetime import datetime
import configparser
import os
from OpenPreferences import OpenPreferences
from OpenLocalFile import OpenLocalFile
from OpenRemoteFile import OpenRemoteFile
from OpenXtream import OpenXtream
import requests
import tools

margin = 10


class MainWindow(QMainWindow, Ui_MainWindow):
    config_file: str = "config.ini"
    main_title: str = "IPTV Playlist Browser"
    git_repo_url: str = "https://github.com/PhunkyBob/iptv_playlist_browser"
    latest_version_url = "https://raw.githubusercontent.com/PhunkyBob/iptv_playlist_browser/master/VERSION"
    pl: Playlist = None
    player_process = None
    current_categ_1: str = ""
    current_categ_2: str = ""
    current_channels = {}
    version: str = ""

    # Config
    config_remember: bool = True
    config_player: str = ""
    config_player_params: str = ""
    config_sep_1: str = ""
    config_sep_2: str = ""
    config_try_xtream_code: bool = True

    # Latest values
    latest_username: str = ""
    latest_password: str = ""
    latest_server: str = ""
    latest_local: str = ""
    latest_remote: str = ""

    def __init__(self, parent=None, version="unkwnown"):
        super().__init__(parent)
        loadUi(tools.resource_path("ui/main_ui.ui"), self)
        # self.setupUi(self)
        self.connect_signals_slots()
        self.pl = None
        self.lbl_wait.hide()
        now = datetime.now()
        self.version = version

        # Set default values
        self.setWindowTitle(f"{self.main_title}")
        self.date_start.setDate(QtCore.QDate(now.year, now.month, now.day))
        self.time_start.setTime(QtCore.QTime(now.hour, (now.minute // 5) * 5))
        self.txt_duration.setText('80')
        self.chk_catchup.setEnabled(False)
        self.date_start.setEnabled(False)
        self.time_start.setEnabled(False)
        self.btn_watch.setEnabled(False)
        self.onlyInt = QtGui.QIntValidator()
        self.txt_duration.setValidator(self.onlyInt)

        # Read config
        config = configparser.ConfigParser()
        if os.path.isfile(self.config_file):
            config.read(self.config_file, encoding="utf-8")
            if "PREFERENCES" in config and "remember_latest" in config["PREFERENCES"]:
                self.config_remember = config["PREFERENCES"]["remember_latest"]
                self.config_remember = (
                    False
                    if self.config_remember.lower() in ("0", "", "n", "no", "false")
                    else True
                )
            if "PREFERENCES" in config and "player" in config["PREFERENCES"]:
                self.config_player = config["PREFERENCES"]["player"]
            if "PREFERENCES" in config and "player_params" in config["PREFERENCES"]:
                self.config_player_params = config["PREFERENCES"]["player_params"]
            if (
                "PREFERENCES" in config
                and "playlist_group_separator" in config["PREFERENCES"]
            ):
                self.config_sep_1 = config["PREFERENCES"]["playlist_group_separator"]
            if (
                "PREFERENCES" in config
                and "playlist_categ_separator" in config["PREFERENCES"]
            ):
                self.config_sep_2 = config["PREFERENCES"]["playlist_categ_separator"]
            if "PREFERENCES" in config and "try_xtream_code" in config["PREFERENCES"]:
                self.config_try_xtream_code = config["PREFERENCES"]["try_xtream_code"]
                self.config_try_xtream_code = (
                    False
                    if self.config_try_xtream_code.lower()
                    in ("0", "", "n", "no", "false")
                    else True
                )
            if "XTREAM_CODE" in config and "username" in config["XTREAM_CODE"]:
                self.latest_username = config["XTREAM_CODE"]["username"]
            if "XTREAM_CODE" in config and "password" in config["XTREAM_CODE"]:
                self.latest_password = config["XTREAM_CODE"]["password"]
            if "XTREAM_CODE" in config and "server" in config["XTREAM_CODE"]:
                self.latest_server = config["XTREAM_CODE"]["server"]
            if "LOCAL" in config and "filepath" in config["LOCAL"]:
                self.latest_local = config["LOCAL"]["filepath"]
            if "REMOTE" in config and "filepath" in config["REMOTE"]:
                self.latest_remote = config["REMOTE"]["filepath"]

        self.save_config()

        # Alert if there is no player already set
        if not os.path.isfile(self.config_player):
            self.warning_player()

    def resizeEvent(self, *args):
        """ Resize and move all elements when window is resized. """
        QMainWindow.resizeEvent(self, *args)
        list_width = int((self.width() - 4 * margin) / 3)
        list_height = self.height() - 200
        self.list_categ_1.resize(list_width, list_height)
        self.list_categ_2.resize(list_width, list_height)
        self.list_channels.resize(list_width, list_height)
        self.txt_filter_groups.resize(list_width - 110, 25)
        self.txt_filter_categories.resize(list_width - 110, 25)
        self.txt_filter_channels.resize(list_width - 110, 25)
        self.txt_url.resize(self.width() - 90 - 3 * margin, 25)
        self.frm_catchup.resize(self.width() - 2 * margin, self.frm_catchup.height())
        self.cmb_epg.resize(
            self.frm_catchup.width() - 410 - margin, self.cmb_epg.height()
        )
        self.list_categ_1.move(1 * margin + 0 * list_width, 40)
        self.list_categ_2.move(2 * margin + 1 * list_width, 40)
        self.list_channels.move(3 * margin + 2 * list_width, 40)
        self.txt_filter_groups.move(self.list_categ_1.pos().x() + 110, margin)
        self.txt_filter_categories.move(self.list_categ_2.pos().x() + 110, margin)
        self.txt_filter_channels.move(self.list_channels.pos().x() + 110, margin)
        self.btn_watch.move(
            self.width() - self.btn_watch.width() - margin, 40 + list_height + margin
        )
        self.txt_url.move(margin, 40 + list_height + margin)
        self.frm_catchup.move(margin, 65 + list_height + 2 * margin)
        self.lbl_groups.move(self.list_categ_1.pos().x(), 15)
        self.lbl_categories.move(self.list_categ_2.pos().x(), 15)
        self.lbl_channels.move(self.list_channels.pos().x(), 15)

    def connect_signals_slots(self):
        """ Link elements signals to functions. """
        self.action_Exit.triggered.connect(self.close)
        self.action_Open_local_file.triggered.connect(self.open_local_file)
        self.action_Open_remote_file.triggered.connect(self.open_remote_file)
        self.action_api.triggered.connect(self.open_xtream)
        self.action_About.triggered.connect(self.about)
        self.action_Preferences.triggered.connect(self.preferences)
        self.list_categ_1.itemSelectionChanged.connect(self.select_group)
        self.list_categ_2.itemSelectionChanged.connect(self.select_category)
        self.list_channels.itemSelectionChanged.connect(self.select_channel)
        self.list_channels.doubleClicked.connect(self.watch)
        self.btn_watch.clicked.connect(self.watch)
        self.txt_filter_groups.textChanged.connect(self.update_groups)
        self.txt_filter_categories.textChanged.connect(self.update_categories)
        self.txt_filter_channels.textChanged.connect(self.update_channels)
        self.chk_catchup.stateChanged.connect(self.change_catchup_settings)
        self.date_start.dateChanged.connect(self.change_catchup_settings)
        self.time_start.timeChanged.connect(self.change_catchup_settings)
        self.txt_duration.textChanged.connect(self.change_catchup_settings)
        self.txt_url.textChanged.connect(self.url_changed)
        self.cmb_epg.currentIndexChanged.connect(self.select_epg)

    def preferences(self):
        """ Open "preferences" dialog. """
        dialog = OpenPreferences(
            self,
            self.config_player,
            self.config_player_params,
            self.config_remember,
            self.config_try_xtream_code,
            self.config_sep_1,
            self.config_sep_2,
        )
        dialog.exec()
        if dialog.validated:
            # Dialog closed with "OK" --> save parameters
            self.config_player = dialog.player
            self.config_player_params = dialog.player_params
            self.config_remember = dialog.remember_latest
            self.config_try_xtream_code = dialog.try_xtream_code
            self.config_sep_1 = dialog.playlist_group_separator
            self.config_sep_2 = dialog.playlist_category_separator
            self.save_config()

    def open_local_file(self):
        """ Open "open local file" dialog. """
        dialog = OpenLocalFile(self, self.latest_local, self.config_remember)
        dialog.exec()
        if dialog.remember and dialog.url:
            self.latest_local = dialog.url
            self.save_config()
        if dialog.url:
            self.open_file(
                filename=dialog.url,
                try_xtream=self.config_try_xtream_code,
                sep_lvl1=self.config_sep_1,
                sep_lvl2=self.config_sep_2,
            )

    def open_remote_file(self):
        """ Open "open remote file" dialog. """
        dialog = OpenRemoteFile(self, self.latest_remote, self.config_remember)
        dialog.exec()
        if dialog.remember and dialog.url:
            self.latest_remote = dialog.url
            self.save_config()
        if dialog.url:
            self.open_file(
                filename=dialog.url,
                try_xtream=self.config_try_xtream_code,
                sep_lvl1=self.config_sep_1,
                sep_lvl2=self.config_sep_2,
            )

    def open_xtream(self):
        """ Open "Xtream code" dialog. """
        dialog = OpenXtream(
            self,
            self.latest_username,
            self.latest_password,
            self.latest_server,
            self.config_remember,
        )
        dialog.exec()
        if dialog.remember and dialog.username and dialog.password and dialog.password:
            self.latest_username = dialog.username
            self.latest_password = dialog.password
            self.latest_server = dialog.server
            self.save_config()
        if dialog.username:
            self.open_file(
                server=dialog.server,
                username=dialog.username,
                password=dialog.password,
                sep_lvl1=self.config_sep_1,
                sep_lvl2=self.config_sep_2,
            )

    def open_file(
        self,
        server="",
        username="",
        password="",
        filename="",
        try_xtream=True,
        sep_lvl1="▼---",
        sep_lvl2="---●★",
    ):
        """ Get the playlist from the file or the Xtream credentials. """
        self.show_loader()
        # Update title window.
        if filename:
            self.setWindowTitle(f"{self.main_title} - {filename}")
        if server:
            self.setWindowTitle(f"{self.main_title} - {username}@{server}")

        self.pl = Playlist(
            server=server,
            username=username,
            password=password,
            filename=filename,
            try_xtream=try_xtream,
            sep_lvl1=sep_lvl1,
            sep_lvl2=sep_lvl2,
        )
        # Reset current selections and content.
        self.current_categ_1 = ""
        self.current_categ_2 = ""
        self.current_channels = {}
        self.list_categ_1.setCurrentItem(None)
        self.list_categ_1.clear()
        self.list_categ_2.setCurrentItem(None)
        self.list_categ_2.clear()
        self.list_channels.setCurrentItem(None)
        self.list_channels.clear()
        self.update_groups()
        if not self.pl.api_account:
            self.chk_catchup.setEnabled(False)
            self.date_start.setEnabled(False)
            self.time_start.setEnabled(False)
        else:
            self.chk_catchup.setEnabled(True)
            self.date_start.setEnabled(True)
            self.time_start.setEnabled(True)
        self.hide_loader()

    def about(self):
        """ Open "about" dialog. """
        # Check what is the latest version available in GitHub
        latest_msg = self.check_version()
        QMessageBox.about(
            self,
            "IPTV Playlist Browser",
            "<p>A simple app to browse your IPTV playlist.</p>"
            + f"<p>Version {self.version}{latest_msg}</p>"
            + f'<p><a href="{self.git_repo_url}">{self.git_repo_url}</a></p>',
        )

    def warning_player(self):
        """ Open "warning" dialog when any player is specified. """
        QMessageBox.about(
            self,
            "IPTV Playlist Browser - WARNING",
            "<p>The application doesn't know how to play the video files. </p>"
            + '<p>Please go to "<i><b>Preferences...</b></i>" menu and set the path for your desired player. </p>',
        )

    def check_version(self):
        """ Check what is the latest version on GitHub. """
        res = requests.get(self.latest_version_url)
        latest = ""
        if res.status_code != 200:
            return latest
        else:
            latest_version = res.text.strip()
            if latest_version == self.version:
                return " (latest)"
            else:
                return f" ({latest} available)"

    def update_groups(self):
        """ Update the list "groups" with available / filtered elements. """
        fltr = self.txt_filter_groups.text()
        self.list_categ_1.setCurrentItem(None)
        self.list_categ_1.clear()
        for categ_1 in self.pl.channels:
            if fltr.lower() in categ_1.lower() and len(self.pl.channels[categ_1]) > 0:
                self.list_categ_1.addItem(categ_1)
        self.lbl_groups.setText(f"Groups ({self.list_categ_1.count()})")

    def update_categories(self):
        """ Update the list "categories" with available / filtered elements. """
        fltr = self.txt_filter_categories.text()
        self.list_categ_2.setCurrentItem(None)
        self.list_categ_2.clear()
        if self.current_categ_1:
            for categ_2 in self.pl.channels[self.current_categ_1]:
                if (
                    fltr.lower() in categ_2.lower()
                    and len(self.pl.channels[self.current_categ_1][categ_2]) > 0
                ):
                    self.list_categ_2.addItem(categ_2)
        self.lbl_categories.setText(f"Categories ({self.list_categ_2.count()})")

    def update_channels(self):
        """ Update the list "channels" with available / filtered elements. """
        fltr = self.txt_filter_channels.text()
        self.list_channels.setCurrentItem(None)
        self.list_channels.clear()
        self.current_channels = {}

        if self.current_categ_2:
            for channel in self.pl.channels[self.current_categ_1][self.current_categ_2]:
                if fltr.lower() in channel.lower():
                    self.list_channels.addItem(channel)
                    self.current_channels[channel] = self.pl.channels[
                        self.current_categ_1
                    ][self.current_categ_2][channel]
        else:
            # If no category is selected, display all available channels.
            for i in range(self.list_categ_2.count()):
                categ_2 = self.list_categ_2.item(i).text()
                for channel in self.pl.channels[self.current_categ_1][categ_2]:
                    if fltr.lower() in channel.lower():
                        self.list_channels.addItem(channel)
                        self.current_channels[channel] = self.pl.channels[
                            self.current_categ_1
                        ][categ_2][channel]
        self.lbl_channels.setText(f"Channels ({self.list_channels.count()})")

    def select_group(self):
        """ When a group is selected. """
        self.show_loader()
        self.current_categ_1 = ""
        if self.list_categ_1.currentItem():
            self.current_categ_1 = self.list_categ_1.currentItem().text()
        self.current_categ_2 = ""
        self.list_categ_2.setCurrentItem(None)
        self.list_categ_2.clear()
        self.update_categories()
        self.update_channels()
        self.hide_loader()

    def select_category(self):
        """ When a category is selected. """
        self.show_loader()
        self.list_channels.setCurrentItem(None)
        self.list_channels.clear()
        self.txt_url.setText("")
        if self.list_categ_2.currentItem():
            self.current_categ_2 = self.list_categ_2.currentItem().text()
            # print(self.current_categ_2)
            self.update_channels()
        self.hide_loader()

    def select_channel(self):
        """ When a channel is selected. """
        self.show_loader()
        if self.list_channels.currentItem():
            channel = self.list_channels.currentItem().text()
            url = self.current_channels[channel]
            # Enable / disable catchup
            self.chk_catchup.setEnabled(False)
            self.lbl_catchup.setText("No catchup available")
            if (
                url in self.pl.channels_details
                and self.pl.channels_details[url]["tv_archive"]
            ):
                self.chk_catchup.setEnabled(True)
                self.lbl_catchup.setText(f"Catchup available")
                if self.pl.channels_details[url]["stream_id"]:
                    self.update_epg(self.pl.channels_details[url]["stream_id"])
                else:
                    self.cmb_epg.clear()
            else:
                self.cmb_epg.clear()

            self.change_catchup_settings()
        self.hide_loader()

    def change_catchup_settings(self):
        """ Decide what URL should be displayed between live and catchup. """
        show_catchup = self.chk_catchup.isChecked()
        self.date_start.setVisible(show_catchup)
        self.time_start.setVisible(show_catchup)
        self.txt_duration.setVisible(show_catchup)
        self.cmb_epg.setVisible(show_catchup)

        if self.list_channels.currentItem():
            channel = self.list_channels.currentItem().text()
            url = self.current_channels[channel]
            if self.chk_catchup.isChecked() and self.chk_catchup.isEnabled():
                if self.pl.channels_details[url]["stream_id"]:
                    stream = self.pl.channels_details[url]["stream_id"]
                    server = self.pl.api_account["server_info"]["url"]
                    protocol = self.pl.api_account["server_info"]["server_protocol"]
                    port = self.pl.api_account["server_info"]["port"]
                    username = self.pl.api_account["user_info"]["username"]
                    password = self.pl.api_account["user_info"]["password"]
                    date = self.date_start.text()
                    time = self.time_start.text().replace(":", "-")
                    duration = self.txt_duration.text()
                    url = f"{protocol}://{server}:{port}/streaming/timeshift.php?username={username}&password={password}&stream={stream}&start={date}:{time}&duration={duration}"
            self.txt_url.setText(url)

    def update_epg(self, stream):
        """ Update the EPG for current channel and add elements in the list. """
        self.pl.update_epg(stream)
        self.cmb_epg.clear()
        self.cmb_epg.addItem("...")
        for elem in reversed(sorted(self.pl.channels_epg[stream].keys())):
            self.cmb_epg.addItem(elem, self.pl.channels_epg[stream][elem])

    def select_epg(self):
        """ When user selects a program in EPG, update the catchup settings. """
        item = self.cmb_epg.currentData()
        if item:
            self.date_start.setDate(
                QtCore.QDate.fromString(item["start_date"], QtCore.Qt.ISODate)
            )
            self.time_start.setTime(QtCore.QTime.fromString(item["start_time"]))
            self.txt_duration.setText(str(item["duration"]))
            self.change_catchup_settings()

    def watch(self):
        """ "Launch player with correct parameters. """
        url = self.txt_url.text()
        if self.player_process:
            # Kill the previous process because we don't want more than 1 player
            try:
                process = psutil.Process(self.player_process.pid)
                for proc in process.children(recursive=True):
                    try:
                        proc.kill()
                    except:
                        pass
            except:
                pass
            self.player_process = None
        # Create a new process in a separated thread
        self.player_process = subprocess.Popen(
            [self.config_player, url.replace("&", "^&"), self.config_player_params],
            shell=True,
        )

    def show_loader(self):
        """ Display the loader. """
        self.lbl_wait.show()
        self.lbl_wait.repaint()

    def hide_loader(self):
        """ Hide the loader. """
        self.lbl_wait.hide()
        self.lbl_wait.repaint()

    def save_config(self):
        """ Save the current parameters to a config file. """
        config = configparser.ConfigParser()
        config["PREFERENCES"] = {}
        config["PREFERENCES"]["remember_latest"] = str(self.config_remember)
        config["PREFERENCES"]["player"] = self.config_player
        config["PREFERENCES"]["player_params"] = self.config_player_params
        config["PREFERENCES"]["try_xtream_code"] = str(self.config_try_xtream_code)
        config["PREFERENCES"]["playlist_group_separator"] = self.config_sep_1
        config["PREFERENCES"]["playlist_categ_separator"] = self.config_sep_2

        config["XTREAM_CODE"] = {}
        config["XTREAM_CODE"]["username"] = self.latest_username
        config["XTREAM_CODE"]["password"] = self.latest_password
        config["XTREAM_CODE"]["server"] = self.latest_server

        config["LOCAL"] = {}
        config["LOCAL"]["filepath"] = self.latest_local
        config["REMOTE"] = {}
        config["REMOTE"]["filepath"] = self.latest_remote

        with open(self.config_file, "w", encoding="utf-8") as configfile:
            config.write(configfile)

    def url_changed(self):
        """ When the URL is changed, enable / disable the "Watch" button. """
        if self.txt_url.text():
            self.btn_watch.setEnabled(True)
        else:
            self.btn_watch.setEnabled(False)
