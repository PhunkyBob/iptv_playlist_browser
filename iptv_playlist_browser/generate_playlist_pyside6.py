# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generate_playlist.ui'
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
        Dialog.setEnabled(True)
        Dialog.resize(510, 180)
        Dialog.setMinimumSize(QSize(510, 180))
        Dialog.setMaximumSize(QSize(16777215, 180))
        self.chk_live = QCheckBox(Dialog)
        self.chk_live.setObjectName(u"chk_live")
        self.chk_live.setGeometry(QRect(180, 70, 81, 20))
        self.chk_vod = QCheckBox(Dialog)
        self.chk_vod.setObjectName(u"chk_vod")
        self.chk_vod.setGeometry(QRect(300, 70, 81, 20))
        self.chk_series = QCheckBox(Dialog)
        self.chk_series.setObjectName(u"chk_series")
        self.chk_series.setEnabled(False)
        self.chk_series.setGeometry(QRect(420, 70, 81, 20))
        self.lbl_categories = QLabel(Dialog)
        self.lbl_categories.setObjectName(u"lbl_categories")
        self.lbl_categories.setGeometry(QRect(20, 70, 171, 16))
        self.lbl_url = QLabel(Dialog)
        self.lbl_url.setObjectName(u"lbl_url")
        self.lbl_url.setGeometry(QRect(10, 25, 55, 16))
        self.txt_url = QLineEdit(Dialog)
        self.txt_url.setObjectName(u"txt_url")
        self.txt_url.setGeometry(QRect(50, 21, 391, 25))
        self.btn_browse = QPushButton(Dialog)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setGeometry(QRect(460, 19, 31, 28))
        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(410, 140, 93, 28))
        self.btn_ok = QPushButton(Dialog)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(300, 140, 93, 28))
        self.lbl_group_filter = QLabel(Dialog)
        self.lbl_group_filter.setObjectName(u"lbl_group_filter")
        self.lbl_group_filter.setGeometry(QRect(20, 110, 71, 16))
        self.txt_group_filter = QLineEdit(Dialog)
        self.txt_group_filter.setObjectName(u"txt_group_filter")
        self.txt_group_filter.setGeometry(QRect(90, 110, 151, 21))
        self.txt_title_filter = QLineEdit(Dialog)
        self.txt_title_filter.setObjectName(u"txt_title_filter")
        self.txt_title_filter.setGeometry(QRect(350, 110, 150, 21))
        self.lbl_title_filter = QLabel(Dialog)
        self.lbl_title_filter.setObjectName(u"lbl_title_filter")
        self.lbl_title_filter.setGeometry(QRect(280, 110, 71, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generate playlist", None))
        self.chk_live.setText(QCoreApplication.translate("Dialog", u"Live", None))
        self.chk_vod.setText(QCoreApplication.translate("Dialog", u"VOD", None))
        self.chk_series.setText(QCoreApplication.translate("Dialog", u"Series", None))
        self.lbl_categories.setText(QCoreApplication.translate("Dialog", u"Categories to include:", None))
        self.lbl_url.setText(QCoreApplication.translate("Dialog", u"File", None))
        self.txt_url.setPlaceholderText(QCoreApplication.translate("Dialog", u"c:\\some\\path\\playlist.m3u", None))
        self.btn_browse.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.lbl_group_filter.setText(QCoreApplication.translate("Dialog", u"Group filter: ", None))
#if QT_CONFIG(tooltip)
        self.txt_group_filter.setToolTip(QCoreApplication.translate("Dialog", u"Filter the groups to export, separated by commas.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.txt_title_filter.setToolTip(QCoreApplication.translate("Dialog", u"Filter the titles to export, separated by commas.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_title_filter.setText(QCoreApplication.translate("Dialog", u"Title filter:", None))
    # retranslateUi

