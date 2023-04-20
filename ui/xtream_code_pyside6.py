# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'xtream_code.ui'
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
        Dialog.resize(359, 180)
        Dialog.setMinimumSize(QSize(330, 180))
        Dialog.setMaximumSize(QSize(16777215, 180))
        self.btn_ok = QPushButton(Dialog)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(150, 140, 93, 28))
        self.chk_save = QCheckBox(Dialog)
        self.chk_save.setObjectName(u"chk_save")
        self.chk_save.setGeometry(QRect(10, 140, 131, 20))
        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(250, 140, 93, 28))
        self.txt_username = QLineEdit(Dialog)
        self.txt_username.setObjectName(u"txt_username")
        self.txt_username.setGeometry(QRect(110, 20, 231, 25))
        self.txt_password = QLineEdit(Dialog)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(110, 60, 231, 25))
        self.txt_server = QLineEdit(Dialog)
        self.txt_server.setObjectName(u"txt_server")
        self.txt_server.setGeometry(QRect(110, 100, 231, 25))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 25, 101, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 65, 101, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 105, 101, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Xtream Code", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.chk_save.setText(QCoreApplication.translate("Dialog", u"Remember", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.txt_username.setPlaceholderText(QCoreApplication.translate("Dialog", u"Username", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.txt_server.setPlaceholderText(QCoreApplication.translate("Dialog", u"http://server:port", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Server:port", None))
    # retranslateUi

