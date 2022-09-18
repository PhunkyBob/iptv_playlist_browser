# -*- coding: utf-8 -*-
"""
This class allows to display the "Open remote file" dialog box.
"""

import validators
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from constant import BASE_DIR, MARGIN


class OpenRemoteFile(QDialog):
    url: str = ""
    remember: bool = False

    def __init__(self, parent=None, url="", remember=False):
        super().__init__(parent)
        loadUi(f"{BASE_DIR}/ui/remote_file.ui", self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setMaximumHeight(self.height())
        self.txt_url.setText(url)
        self.chk_save.setChecked(remember)
        self.connect_signals_slots()
        self.verif_fields()

    def resizeEvent(self, *args):
        """ Resize and move all elements when window is resized. """
        QDialog.resizeEvent(self, *args)
        self.txt_url.resize(self.width() - 50 - MARGIN, 25)
        self.btn_ok.move(
            self.width() - self.btn_ok.width() - self.btn_cancel.width() - 2 * MARGIN,
            60,
        )
        self.btn_cancel.move(self.width() - self.btn_cancel.width() - 1 * MARGIN, 60)

    def connect_signals_slots(self):
        """ Link elements signals to functions. """
        self.btn_cancel.clicked.connect(self.close)
        self.btn_ok.clicked.connect(self.click_ok)
        self.txt_url.textChanged.connect(self.verif_fields)

    def click_ok(self):
        """ When button "OK" is clicked, save the values. """
        self.url = self.txt_url.text()
        self.remember = self.chk_save.isChecked()
        self.close()

    def verif_fields(self):
        """ Enable the "OK" button only when all fields are correct. """
        self.btn_ok.setEnabled(
            len(self.txt_url.text()) > 0
            and validators.url(self.txt_url.text(), public=True)
            and not self.txt_url.text().endswith("/")
            and self.txt_url.text().startswith("http") or self.txt_url.text().startswith("https")
        )
