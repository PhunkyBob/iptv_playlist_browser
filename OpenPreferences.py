# -*- coding: utf-8 -*-
"""
This class allows to display the "Preferences" dialog box.
"""

from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui
import os 
import tools

class OpenPreferences(QDialog):
    remember_latest: bool = True
    player: str = ""
    player_params: str = ""
    try_xtream_code: bool = True
    playlist_group_separator: str = ""
    playlist_category_separator: str = ""
    playlist_separator_changed: bool = False
    catchup_add_minutes: int = 0
    validated: bool = False

    def __init__(
        self,
        parent=None,
        player="",
        player_params="",
        remember_latest=True,
        try_xtream_code=True,
        playlist_group_separator="",
        playlist_category_separator="",
        catchup_add_minutes=0
    ):
        super().__init__(parent)
        loadUi(tools.resource_path("ui/preferences.ui"), self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setFixedSize(self.size())
        self.chk_remember.setChecked(remember_latest)
        self.chk_xtream.setChecked(try_xtream_code)
        self.txt_player.setText(player)
        self.txt_player_params.setText(player_params)
        self.txt_pl_sep_1.setText(playlist_group_separator)
        self.txt_pl_sep_2.setText(playlist_category_separator)
        self.txt_catchup_min.setText(str(catchup_add_minutes))
        self.remember_latest = remember_latest
        self.player = player
        self.player_params = player_params
        self.playlist_group_separator = playlist_group_separator
        self.playlist_category_separator = playlist_category_separator
        self.verif_player()
        self.onlyInt = QtGui.QIntValidator()
        self.txt_catchup_min.setValidator(self.onlyInt)
        self.connect_signals_slots()
        

    def resizeEvent(self, *args):
        """ Resize and move all elements when window is resized. """
        QDialog.resizeEvent(self, *args)

    def connect_signals_slots(self):
        """ Link elements signals to functions. """
        self.btn_cancel.clicked.connect(self.close)
        self.btn_ok.clicked.connect(self.click_ok)
        self.btn_browse_player.clicked.connect(self.open_filename_dialog)
        self.txt_player.textChanged.connect(self.verif_player)


    def open_filename_dialog(self):
        """ Choose a player binary file. """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Choose player executable",
            "",
            "Player (*.exe);;All Files (*)",
            options=options,
        )
        if filename:
            self.txt_player.setText(filename)

    def click_ok(self):
        """ When button "OK" is clicked, save the values. """
        self.playlist_separator_changed = (
            self.playlist_group_separator != self.txt_pl_sep_1.text()
            or self.playlist_category_separator != self.txt_pl_sep_2.text()
        )
        self.remember_latest = self.chk_remember.isChecked()
        self.try_xtream_code = self.chk_xtream.isChecked()
        self.player = self.txt_player.text()
        self.player_params = self.txt_player_params.text()
        self.playlist_group_separator = self.txt_pl_sep_1.text()
        self.playlist_category_separator = self.txt_pl_sep_2.text()
        self.catchup_add_minutes = int(self.txt_catchup_min.text())
        self.validated = True
        self.close()

    def verif_player(self):
        """ Check if the path is valid and warn if not. """
        if not os.path.isfile(self.txt_player.text()):
            self.txt_player.setStyleSheet("border: 1px solid red;")
        else:
            self.txt_player.setStyleSheet("")