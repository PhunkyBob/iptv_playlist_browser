# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(622, 417)
        self.grp_playlist = QGroupBox(Dialog)
        self.grp_playlist.setObjectName(u"grp_playlist")
        self.grp_playlist.setGeometry(QRect(10, 180, 601, 101))
        self.txt_pl_sep_1 = QLineEdit(self.grp_playlist)
        self.txt_pl_sep_1.setObjectName(u"txt_pl_sep_1")
        self.txt_pl_sep_1.setGeometry(QRect(130, 60, 151, 25))
        self.txt_pl_sep_2 = QLineEdit(self.grp_playlist)
        self.txt_pl_sep_2.setObjectName(u"txt_pl_sep_2")
        self.txt_pl_sep_2.setGeometry(QRect(450, 60, 141, 25))
        self.lbl_pl_sep_1 = QLabel(self.grp_playlist)
        self.lbl_pl_sep_1.setObjectName(u"lbl_pl_sep_1")
        self.lbl_pl_sep_1.setGeometry(QRect(10, 65, 101, 16))
        self.lbl_pl_sep_2 = QLabel(self.grp_playlist)
        self.lbl_pl_sep_2.setObjectName(u"lbl_pl_sep_2")
        self.lbl_pl_sep_2.setGeometry(QRect(320, 65, 121, 16))
        self.chk_xtream = QCheckBox(self.grp_playlist)
        self.chk_xtream.setObjectName(u"chk_xtream")
        self.chk_xtream.setGeometry(QRect(10, 20, 271, 20))
        self.grp_general = QGroupBox(Dialog)
        self.grp_general.setObjectName(u"grp_general")
        self.grp_general.setGeometry(QRect(10, 10, 601, 141))
        self.chk_remember = QCheckBox(self.grp_general)
        self.chk_remember.setObjectName(u"chk_remember")
        self.chk_remember.setGeometry(QRect(20, 100, 161, 20))
        self.lbl_player = QLabel(self.grp_general)
        self.lbl_player.setObjectName(u"lbl_player")
        self.lbl_player.setGeometry(QRect(10, 25, 91, 16))
        self.txt_player = QLineEdit(self.grp_general)
        self.txt_player.setObjectName(u"txt_player")
        self.txt_player.setGeometry(QRect(159, 20, 391, 25))
        self.btn_browse_player = QPushButton(self.grp_general)
        self.btn_browse_player.setObjectName(u"btn_browse_player")
        self.btn_browse_player.setGeometry(QRect(560, 20, 31, 28))
        self.lbl_player_params = QLabel(self.grp_general)
        self.lbl_player_params.setObjectName(u"lbl_player_params")
        self.lbl_player_params.setGeometry(QRect(10, 65, 141, 16))
        self.txt_player_params = QLineEdit(self.grp_general)
        self.txt_player_params.setObjectName(u"txt_player_params")
        self.txt_player_params.setGeometry(QRect(160, 60, 431, 25))
        self.btn_ok = QPushButton(Dialog)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(420, 380, 93, 28))
        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(520, 380, 93, 28))
        self.grp_catchup = QGroupBox(Dialog)
        self.grp_catchup.setObjectName(u"grp_catchup")
        self.grp_catchup.setGeometry(QRect(10, 310, 601, 61))
        self.txt_catchup_min = QLineEdit(self.grp_catchup)
        self.txt_catchup_min.setObjectName(u"txt_catchup_min")
        self.txt_catchup_min.setGeometry(QRect(240, 20, 51, 22))
        self.lbl_add_minutes = QLabel(self.grp_catchup)
        self.lbl_add_minutes.setObjectName(u"lbl_add_minutes")
        self.lbl_add_minutes.setGeometry(QRect(10, 20, 231, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Preferences", None))
        self.grp_playlist.setTitle(QCoreApplication.translate("Dialog", u"Playlist", None))
        self.lbl_pl_sep_1.setText(QCoreApplication.translate("Dialog", u"Group separator", None))
        self.lbl_pl_sep_2.setText(QCoreApplication.translate("Dialog", u"Category separator", None))
        self.chk_xtream.setText(QCoreApplication.translate("Dialog", u"Always try to retreive Xtream Code", None))
        self.grp_general.setTitle(QCoreApplication.translate("Dialog", u"General", None))
        self.chk_remember.setText(QCoreApplication.translate("Dialog", u"Remember latest input", None))
        self.lbl_player.setText(QCoreApplication.translate("Dialog", u"Video player", None))
        self.btn_browse_player.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.lbl_player_params.setText(QCoreApplication.translate("Dialog", u"Additional parameters", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.grp_catchup.setTitle(QCoreApplication.translate("Dialog", u"Catchup", None))
        self.lbl_add_minutes.setText(QCoreApplication.translate("Dialog", u"Always add minutes to current EPG", None))
    # retranslateUi

