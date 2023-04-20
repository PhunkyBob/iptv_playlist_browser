# -*- coding: utf-8 -*-
import sys
import os
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from typing import Any


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def loadUi(ui_path: str, object: Any = None) -> None:
    """Load a Qt UI file into a Qt object."""
    loader = QUiLoader()
    ui_file = QFile(resource_path(ui_path))
    ui_file.open(QFile.ReadOnly)
    ui = loader.load(ui_file, object)
    ui_file.close()
    return ui
