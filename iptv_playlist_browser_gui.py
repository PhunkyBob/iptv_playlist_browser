# -*- coding: utf-8 -*-
"""
Run the GUI.
"""

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

__version__ = "1.03.0"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow(version=__version__)
    win.show()
    sys.exit(app.exec())
