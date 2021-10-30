# -*- coding: utf-8 -*-
"""
This class allows to display the "Open Xtream Code" dialog box.
"""

from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import tools

margin = 10

class OpenXtream(QDialog):
    username: str = ""
    password: str = ""
    server: str = ""
    remember: bool = False

    def __init__(
        self, parent=None, username="", password="", server="", remember=False
    ):
        super().__init__(parent)
        loadUi(tools.resource_path("ui/xtream_code.ui"), self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setMaximumHeight(self.height())
        self.txt_server.setText(server)
        self.txt_username.setText(username)
        self.txt_password.setText(password)
        self.chk_save.setChecked(remember)
        self.connect_signals_slots()
        self.verif_fields()

    def resizeEvent(self, *args):
        """ Resize and move all elements when window is resized. """
        QDialog.resizeEvent(self, *args)
        self.txt_server.resize(self.width() - 110 - margin, 25)
        self.txt_username.resize(self.width() - 110 - margin, 25)
        self.txt_password.resize(self.width() - 110 - margin, 25)
        self.btn_ok.move(
            self.width() - self.btn_ok.width() - self.btn_cancel.width() - 2 * margin,
            140,
        )
        self.btn_cancel.move(self.width() - self.btn_cancel.width() - 1 * margin, 140)

    def connect_signals_slots(self):
        """ Link elements signals to functions. """
        self.btn_cancel.clicked.connect(self.close)
        self.btn_ok.clicked.connect(self.click_ok)
        self.txt_username.textChanged.connect(self.verif_fields)
        self.txt_password.textChanged.connect(self.verif_fields)
        self.txt_server.textChanged.connect(self.verif_fields)

    def click_ok(self):
        """ When button "OK" is clicked, save the values. """
        self.username = self.txt_username.text()
        self.password = self.txt_password.text()
        self.server = self.txt_server.text()
        self.remember = self.chk_save.isChecked()
        self.close()

    def verif_fields(self):
        """ Enable the "OK" button only when all fields are correct. """
        self.btn_ok.setEnabled(
            len(self.txt_username.text()) > 0
            and len(self.txt_password.text()) > 0
            and len(self.txt_server.text()) > 0
        )
