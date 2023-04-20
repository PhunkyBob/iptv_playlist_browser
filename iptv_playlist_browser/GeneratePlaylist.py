# -*- coding: utf-8 -*-
"""
This class allows to display the "Open local file" dialog box.
"""

from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6 import QtCore
from .generate_playlist_pyside6 import Ui_Dialog

margin = 10


class GeneratePlaylist(QDialog):
    url: str = ""
    export_live: bool = False
    export_vod: bool = False
    export_series: bool = False

    def __init__(self, parent=None, url=""):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setMinimumHeight(self.height())
        self.setMaximumHeight(self.height())
        self.ui.txt_url.setText(url)
        self.connect_signals_slots()
        self.verif_fields()

    def resizeEvent(self, *args):
        """Resize and move all elements when window is resized."""
        QDialog.resizeEvent(self, *args)
        self.ui.txt_url.resize(self.width() - 50 - self.ui.btn_browse.width() - 2 * margin, 25)
        self.ui.btn_ok.move(
            self.width() - self.ui.btn_ok.width() - self.ui.btn_cancel.width() - 2 * margin,
            self.height() - self.ui.btn_ok.height() - margin,
        )
        self.ui.btn_cancel.move(
            self.width() - self.ui.btn_cancel.width() - 1 * margin,
            self.height() - self.ui.btn_cancel.height() - margin,
        )
        self.ui.btn_browse.move(self.width() - self.ui.btn_browse.width() - 1 * margin, 20)

    def connect_signals_slots(self):
        """Link elements signals to functions."""
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.click_ok)
        self.ui.btn_browse.clicked.connect(self.open_filename_dialog)
        self.ui.txt_url.textChanged.connect(self.verif_fields)
        self.ui.chk_live.stateChanged.connect(self.verif_fields)
        self.ui.chk_vod.stateChanged.connect(self.verif_fields)
        self.ui.chk_series.stateChanged.connect(self.verif_fields)

    def click_ok(self):
        """When button "OK" is clicked, save the values."""
        self.url = self.ui.txt_url.text()
        self.export_live = self.ui.chk_live.isChecked()
        self.export_vod = self.ui.chk_vod.isChecked()
        self.export_series = self.ui.chk_series.isChecked()
        self.close()

    def verif_fields(self):
        """Enable the "OK" button only when all fields are correct."""
        self.ui.btn_ok.setEnabled(
            len(self.ui.txt_url.text()) > 0
            and any([self.ui.chk_live.isChecked(), self.ui.chk_vod.isChecked(), self.ui.chk_series.isChecked()])
        )

    def open_filename_dialog(self):
        """Choose a playlist file."""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Generate playlist",
            "",
            "Playlists (*.m3u);;All Files (*)",
            options=options,
        )
        if filename:
            self.ui.txt_url.setText(filename)
