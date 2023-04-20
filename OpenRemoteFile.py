# -*- coding: utf-8 -*-
"""
This class allows to display the "Open remote file" dialog box.
"""

from PySide6.QtWidgets import QDialog
from PySide6 import QtCore
from ui.remote_file_pyside6 import Ui_Dialog

margin = 10


class OpenRemoteFile(QDialog):
    url: str = ""
    remember: bool = False

    def __init__(self, parent=None, url="", remember=False):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setMaximumHeight(self.height())
        self.ui.txt_url.setText(url)
        self.ui.chk_save.setChecked(remember)
        self.connect_signals_slots()
        self.verif_fields()

    def resizeEvent(self, *args):
        """Resize and move all elements when window is resized."""
        QDialog.resizeEvent(self, *args)
        self.ui.txt_url.resize(self.width() - 50 - margin, 25)
        self.ui.btn_ok.move(
            self.width() - self.ui.btn_ok.width() - self.ui.btn_cancel.width() - 2 * margin,
            60,
        )
        self.ui.btn_cancel.move(self.width() - self.ui.btn_cancel.width() - 1 * margin, 60)

    def connect_signals_slots(self):
        """Link elements signals to functions."""
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.click_ok)
        self.ui.txt_url.textChanged.connect(self.verif_fields)

    def click_ok(self):
        """When button "OK" is clicked, save the values."""
        self.url = self.ui.txt_url.text()
        self.remember = self.ui.chk_save.isChecked()
        self.close()

    def verif_fields(self):
        """Enable the "OK" button only when all fields are correct."""
        self.ui.btn_ok.setEnabled(len(self.ui.txt_url.text()) > 0)
