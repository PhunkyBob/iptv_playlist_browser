# -*- coding: utf-8 -*-
"""
Run the GUI.
"""

import sys
from PySide6.QtWidgets import QApplication
from iptv_playlist_browser.MainWindow import MainWindow
from iptv_playlist_browser import __version__

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow(version=__version__)
    win.show()
    sys.exit(app.exec())
