# -*- coding: utf-8 -*-
"""
This class allows to display the "Open local file" dialog box.
"""

from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import os
import tools

margin = 10


class OpenLocalFile(QDialog):
    url: str = ""
    sep_lvl1: str = ""
    sep_lvl2: str = ""
    remember: bool = False
    preview_lines: int = 30

    def __init__(self, parent=None, url="", remember=False, sep_lvl1="", sep_lvl2=""):
        super().__init__(parent)
        loadUi(tools.resource_path("ui/local_file.ui"), self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setMinimumHeight(self.height())
        self.setMaximumHeight(self.height())
        self.txt_url.setText(url)
        self.chk_save.setChecked(remember)
        self.txt_pl_sep_1.setText(sep_lvl1)
        self.txt_pl_sep_2.setText(sep_lvl2)
        self.connect_signals_slots()
        self.verif_fields()

    def resizeEvent(self, *args):
        """ Resize and move all elements when window is resized. """
        QDialog.resizeEvent(self, *args)
        self.txt_url.resize(
            self.width() - 50 - self.btn_browse.width() - 2 * margin, 25
        )
        self.txt_preview.resize(
            self.width() - 130 - margin, self.txt_preview.height()
        )
        self.btn_ok.move(
            self.width() - self.btn_ok.width() - self.btn_cancel.width() - 2 * margin,
            self.height() - self.btn_ok.height() - margin,
        )
        self.btn_cancel.move(self.width() - self.btn_cancel.width() - 1 * margin, self.height() - self.btn_cancel.height() - margin)
        self.btn_browse.move(self.width() - self.btn_browse.width() - 1 * margin, 20)

    def connect_signals_slots(self):
        """ Link elements signals to functions. """
        self.btn_cancel.clicked.connect(self.close)
        self.btn_ok.clicked.connect(self.click_ok)
        self.btn_browse.clicked.connect(self.open_filename_dialog)
        self.txt_url.textChanged.connect(self.verif_fields)

    def click_ok(self):
        """ When button "OK" is clicked, save the values. """
        self.url = self.txt_url.text()
        self.sep_lvl1 = self.txt_pl_sep_1.text()
        self.sep_lvl2 = self.txt_pl_sep_2.text()
        self.remember = self.chk_save.isChecked()
        self.close()

    def verif_fields(self):
        """ Enable the "OK" button only when all fields are correct. """
        if not os.path.isfile(self.txt_url.text()):
            self.txt_url.setStyleSheet("border: 1px solid red;")
        else:
            self.txt_url.setStyleSheet("")
        self.btn_ok.setEnabled(len(self.txt_url.text()) > 0)

    def verif_file(self):
        """ Check if the path is valid and warn if not. """
        if not os.path.isfile(self.txt_url.text()):
            self.txt_url.setStyleSheet("border: 1px solid red;")
        else:
            self.txt_url.setStyleSheet("")

    def open_filename_dialog(self):
        """ Choose a playlist file. """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open local playlist",
            "",
            "Playlists (*.m3u);;All Files (*)",
            options=options,
        )
        if filename:
            self.txt_url.setText(filename)
            self.update_preview(filename)

    def update_preview(self, filename):
        preview = ""
        self.txt_preview.setText(preview)
        with open(filename, 'r', encoding='utf-8') as f:
            cnt = 0
            while content := f.readline():
                content = content.strip()
                # content = normalize("NFKD", content)
                if not content.startswith('#EXTINF:-1'):
                    continue
                preview += ','.join(content.split(',')[1:]) + "\n"
                cnt += 1
                if  cnt > self.preview_lines:
                    break
        self.txt_preview.setText(preview + '...')

