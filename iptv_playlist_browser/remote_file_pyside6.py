# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remote_file.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(737, 100)
        Dialog.setMinimumSize(QSize(400, 100))
        Dialog.setMaximumSize(QSize(16777215, 100))
        self.txt_url = QLineEdit(Dialog)
        self.txt_url.setObjectName(u"txt_url")
        self.txt_url.setGeometry(QRect(50, 20, 671, 25))
        self.btn_ok = QPushButton(Dialog)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(530, 60, 93, 28))
        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(630, 60, 93, 28))
        self.lbl_url = QLabel(Dialog)
        self.lbl_url.setObjectName(u"lbl_url")
        self.lbl_url.setGeometry(QRect(10, 25, 55, 16))
        self.chk_save = QCheckBox(Dialog)
        self.chk_save.setObjectName(u"chk_save")
        self.chk_save.setGeometry(QRect(50, 60, 131, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Open remote playlist", None))
        self.txt_url.setPlaceholderText(QCoreApplication.translate("Dialog", u"http://server:port/get.php?username=xxx&password=xxx&type=m3u_full&output=mpegts", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.lbl_url.setText(QCoreApplication.translate("Dialog", u"URL", None))
        self.chk_save.setText(QCoreApplication.translate("Dialog", u"Remember", None))
    # retranslateUi

