# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'local_file.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(732, 290)
        Dialog.setMinimumSize(QSize(400, 90))
        self.lbl_url = QLabel(Dialog)
        self.lbl_url.setObjectName(u"lbl_url")
        self.lbl_url.setGeometry(QRect(10, 25, 55, 16))
        self.btn_ok = QPushButton(Dialog)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(530, 250, 93, 28))
        self.txt_url = QLineEdit(Dialog)
        self.txt_url.setObjectName(u"txt_url")
        self.txt_url.setGeometry(QRect(50, 21, 631, 25))
        self.chk_save = QCheckBox(Dialog)
        self.chk_save.setObjectName(u"chk_save")
        self.chk_save.setGeometry(QRect(50, 60, 131, 20))
        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(630, 250, 93, 28))
        self.btn_browse = QPushButton(Dialog)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setGeometry(QRect(690, 20, 31, 28))
        self.txt_preview = QTextEdit(Dialog)
        self.txt_preview.setObjectName(u"txt_preview")
        self.txt_preview.setGeometry(QRect(130, 90, 591, 101))
        self.lbl_preview = QLabel(Dialog)
        self.lbl_preview.setObjectName(u"lbl_preview")
        self.lbl_preview.setGeometry(QRect(10, 90, 101, 16))
        self.txt_pl_sep_2 = QLineEdit(Dialog)
        self.txt_pl_sep_2.setObjectName(u"txt_pl_sep_2")
        self.txt_pl_sep_2.setGeometry(QRect(450, 205, 141, 25))
        self.lbl_pl_sep_2 = QLabel(Dialog)
        self.lbl_pl_sep_2.setObjectName(u"lbl_pl_sep_2")
        self.lbl_pl_sep_2.setGeometry(QRect(320, 210, 121, 16))
        self.txt_pl_sep_1 = QLineEdit(Dialog)
        self.txt_pl_sep_1.setObjectName(u"txt_pl_sep_1")
        self.txt_pl_sep_1.setGeometry(QRect(130, 205, 151, 25))
        self.lbl_pl_sep_1 = QLabel(Dialog)
        self.lbl_pl_sep_1.setObjectName(u"lbl_pl_sep_1")
        self.lbl_pl_sep_1.setGeometry(QRect(10, 210, 101, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Open local playlist", None))
        self.lbl_url.setText(QCoreApplication.translate("Dialog", u"File", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.txt_url.setPlaceholderText(QCoreApplication.translate("Dialog", u"c:\\some\\path\\playlist.m3u", None))
        self.chk_save.setText(QCoreApplication.translate("Dialog", u"Remember", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_browse.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.lbl_preview.setText(QCoreApplication.translate("Dialog", u"Preview names", None))
        self.lbl_pl_sep_2.setText(QCoreApplication.translate("Dialog", u"Category separator", None))
        self.lbl_pl_sep_1.setText(QCoreApplication.translate("Dialog", u"Group separator", None))
    # retranslateUi

