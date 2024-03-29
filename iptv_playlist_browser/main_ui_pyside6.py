# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTimeEdit, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(866, 712)
        MainWindow.setMinimumSize(QSize(700, 400))
        icon = QIcon()
        icon.addFile(u"./resources/play-button.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_api = QAction(MainWindow)
        self.action_api.setObjectName(u"action_api")
        icon1 = QIcon()
        icon1.addFile(u"./resources/login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_api.setIcon(icon1)
        self.action_Open_local_file = QAction(MainWindow)
        self.action_Open_local_file.setObjectName(u"action_Open_local_file")
        icon2 = QIcon()
        icon2.addFile(u"./resources/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Open_local_file.setIcon(icon2)
        self.action_Open_remote_file = QAction(MainWindow)
        self.action_Open_remote_file.setObjectName(u"action_Open_remote_file")
        icon3 = QIcon()
        icon3.addFile(u"./resources/link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Open_remote_file.setIcon(icon3)
        self.action_Preferences = QAction(MainWindow)
        self.action_Preferences.setObjectName(u"action_Preferences")
        icon4 = QIcon()
        icon4.addFile(u"./resources/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Preferences.setIcon(icon4)
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.action_Download_playlist_lite = QAction(MainWindow)
        self.action_Download_playlist_lite.setObjectName(u"action_Download_playlist_lite")
        self.action_Download_playlist_full = QAction(MainWindow)
        self.action_Download_playlist_full.setObjectName(u"action_Download_playlist_full")
        self.action_Generate_playlist = QAction(MainWindow)
        self.action_Generate_playlist.setObjectName(u"action_Generate_playlist")
        self.action_Generate_playlist.setEnabled(False)
        self.action_Account_infos = QAction(MainWindow)
        self.action_Account_infos.setObjectName(u"action_Account_infos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tab_main = QTabWidget(self.centralwidget)
        self.tab_main.setObjectName(u"tab_main")
        self.tab_main.setGeometry(QRect(10, 10, 841, 571))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.lbl_categories = QLabel(self.tab)
        self.lbl_categories.setObjectName(u"lbl_categories")
        self.lbl_categories.setGeometry(QRect(290, 15, 121, 16))
        self.frm_catchup = QFrame(self.tab)
        self.frm_catchup.setObjectName(u"frm_catchup")
        self.frm_catchup.setGeometry(QRect(10, 470, 821, 61))
        self.frm_catchup.setFrameShape(QFrame.StyledPanel)
        self.frm_catchup.setFrameShadow(QFrame.Raised)
        self.time_start = QTimeEdit(self.frm_catchup)
        self.time_start.setObjectName(u"time_start")
        self.time_start.setGeometry(QRect(250, 0, 71, 22))
        self.cmb_epg = QComboBox(self.frm_catchup)
        self.cmb_epg.setObjectName(u"cmb_epg")
        self.cmb_epg.setGeometry(QRect(410, 0, 401, 22))
        self.txt_duration = QLineEdit(self.frm_catchup)
        self.txt_duration.setObjectName(u"txt_duration")
        self.txt_duration.setGeometry(QRect(330, 0, 51, 22))
        self.date_start = QDateEdit(self.frm_catchup)
        self.date_start.setObjectName(u"date_start")
        self.date_start.setGeometry(QRect(130, 0, 110, 22))
        self.chk_catchup = QCheckBox(self.frm_catchup)
        self.chk_catchup.setObjectName(u"chk_catchup")
        self.chk_catchup.setGeometry(QRect(0, 0, 121, 20))
        self.lbl_catchup = QLabel(self.frm_catchup)
        self.lbl_catchup.setObjectName(u"lbl_catchup")
        self.lbl_catchup.setGeometry(QRect(0, 30, 311, 16))
        self.lbl_channels = QLabel(self.tab)
        self.lbl_channels.setObjectName(u"lbl_channels")
        self.lbl_channels.setGeometry(QRect(570, 15, 121, 16))
        self.list_channels = QListWidget(self.tab)
        self.list_channels.setObjectName(u"list_channels")
        self.list_channels.setGeometry(QRect(570, 40, 256, 421))
        self.txt_filter_categories = QLineEdit(self.tab)
        self.txt_filter_categories.setObjectName(u"txt_filter_categories")
        self.txt_filter_categories.setGeometry(QRect(402, 10, 141, 25))
        self.list_categ_2 = QListWidget(self.tab)
        self.list_categ_2.setObjectName(u"list_categ_2")
        self.list_categ_2.setGeometry(QRect(290, 40, 256, 421))
        self.txt_filter_channels = QLineEdit(self.tab)
        self.txt_filter_channels.setObjectName(u"txt_filter_channels")
        self.txt_filter_channels.setGeometry(QRect(682, 10, 141, 25))
        self.lbl_groups = QLabel(self.tab)
        self.lbl_groups.setObjectName(u"lbl_groups")
        self.lbl_groups.setGeometry(QRect(10, 15, 121, 16))
        self.list_categ_1 = QListWidget(self.tab)
        self.list_categ_1.setObjectName(u"list_categ_1")
        self.list_categ_1.setGeometry(QRect(10, 40, 256, 421))
        self.txt_filter_groups = QLineEdit(self.tab)
        self.txt_filter_groups.setObjectName(u"txt_filter_groups")
        self.txt_filter_groups.setGeometry(QRect(120, 10, 141, 25))
        font = QFont()
        font.setPointSize(8)
        self.txt_filter_groups.setFont(font)
        self.tab_main.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.txt_filter_channels_vod = QLineEdit(self.tab_2)
        self.txt_filter_channels_vod.setObjectName(u"txt_filter_channels_vod")
        self.txt_filter_channels_vod.setGeometry(QRect(392, 10, 141, 25))
        self.txt_filter_groups_vod = QLineEdit(self.tab_2)
        self.txt_filter_groups_vod.setObjectName(u"txt_filter_groups_vod")
        self.txt_filter_groups_vod.setGeometry(QRect(120, 10, 141, 25))
        self.txt_filter_groups_vod.setFont(font)
        self.list_categ_vod = QListWidget(self.tab_2)
        self.list_categ_vod.setObjectName(u"list_categ_vod")
        self.list_categ_vod.setGeometry(QRect(10, 40, 256, 471))
        self.list_channels_vod = QListWidget(self.tab_2)
        self.list_channels_vod.setObjectName(u"list_channels_vod")
        self.list_channels_vod.setGeometry(QRect(280, 40, 256, 471))
        self.lbl_channels_vod = QLabel(self.tab_2)
        self.lbl_channels_vod.setObjectName(u"lbl_channels_vod")
        self.lbl_channels_vod.setGeometry(QRect(280, 15, 121, 16))
        self.lbl_groups_vod = QLabel(self.tab_2)
        self.lbl_groups_vod.setObjectName(u"lbl_groups_vod")
        self.lbl_groups_vod.setGeometry(QRect(10, 15, 121, 16))
        self.picture_vod = QLabel(self.tab_2)
        self.picture_vod.setObjectName(u"picture_vod")
        self.picture_vod.setGeometry(QRect(550, 40, 261, 461))
        self.picture_vod.setScaledContents(False)
        self.tab_main.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.lbl_channels_series = QLabel(self.tab_3)
        self.lbl_channels_series.setObjectName(u"lbl_channels_series")
        self.lbl_channels_series.setGeometry(QRect(288, 15, 121, 16))
        self.lbl_groups_series = QLabel(self.tab_3)
        self.lbl_groups_series.setObjectName(u"lbl_groups_series")
        self.lbl_groups_series.setGeometry(QRect(18, 15, 121, 16))
        self.txt_filter_groups_series = QLineEdit(self.tab_3)
        self.txt_filter_groups_series.setObjectName(u"txt_filter_groups_series")
        self.txt_filter_groups_series.setGeometry(QRect(128, 10, 141, 25))
        self.txt_filter_groups_series.setFont(font)
        self.list_channels_series = QListWidget(self.tab_3)
        self.list_channels_series.setObjectName(u"list_channels_series")
        self.list_channels_series.setGeometry(QRect(288, 40, 256, 471))
        self.list_categ_series = QListWidget(self.tab_3)
        self.list_categ_series.setObjectName(u"list_categ_series")
        self.list_categ_series.setGeometry(QRect(18, 40, 256, 471))
        self.txt_filter_channels_series = QLineEdit(self.tab_3)
        self.txt_filter_channels_series.setObjectName(u"txt_filter_channels_series")
        self.txt_filter_channels_series.setGeometry(QRect(400, 10, 141, 25))
        self.list_episodes = QListWidget(self.tab_3)
        self.list_episodes.setObjectName(u"list_episodes")
        self.list_episodes.setGeometry(QRect(560, 40, 256, 471))
        self.tab_main.addTab(self.tab_3, "")
        self.txt_url = QLineEdit(self.centralwidget)
        self.txt_url.setObjectName(u"txt_url")
        self.txt_url.setEnabled(True)
        self.txt_url.setGeometry(QRect(10, 590, 731, 25))
        self.txt_url.setReadOnly(True)
        self.btn_watch = QPushButton(self.centralwidget)
        self.btn_watch.setObjectName(u"btn_watch")
        self.btn_watch.setGeometry(QRect(750, 590, 93, 25))
        self.lbl_wait = QLabel(self.centralwidget)
        self.lbl_wait.setObjectName(u"lbl_wait")
        self.lbl_wait.setGeometry(QRect(20, 150, 831, 241))
        font1 = QFont()
        font1.setPointSize(28)
        self.lbl_wait.setFont(font1)
        self.lbl_wait.setFrameShape(QFrame.NoFrame)
        self.lbl_wait.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 866, 26))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_About = QMenu(self.menubar)
        self.menu_About.setObjectName(u"menu_About")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuXtream = QMenu(self.menuTools)
        self.menuXtream.setObjectName(u"menuXtream")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.menu_File.addAction(self.action_api)
        self.menu_File.addAction(self.action_Open_local_file)
        self.menu_File.addAction(self.action_Open_remote_file)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Preferences)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_About.addAction(self.action_About)
        self.menuTools.addAction(self.menuXtream.menuAction())
        self.menuTools.addAction(self.action_Generate_playlist)
        self.menuXtream.addAction(self.action_Account_infos)
        self.menuXtream.addAction(self.action_Download_playlist_lite)
        self.menuXtream.addAction(self.action_Download_playlist_full)
        self.toolBar.addAction(self.action_api)
        self.toolBar.addAction(self.action_Open_local_file)
        self.toolBar.addAction(self.action_Open_remote_file)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Preferences)

        self.retranslateUi(MainWindow)

        self.tab_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Playlist Browser", None))
        self.action_api.setText(QCoreApplication.translate("MainWindow", u"&Xtream Code API...", None))
#if QT_CONFIG(tooltip)
        self.action_api.setToolTip(QCoreApplication.translate("MainWindow", u"Xtream Code API", None))
#endif // QT_CONFIG(tooltip)
        self.action_Open_local_file.setText(QCoreApplication.translate("MainWindow", u"&Open local file...", None))
#if QT_CONFIG(shortcut)
        self.action_Open_local_file.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_Open_remote_file.setText(QCoreApplication.translate("MainWindow", u"Open &remote file...", None))
#if QT_CONFIG(shortcut)
        self.action_Open_remote_file.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_Preferences.setText(QCoreApplication.translate("MainWindow", u"&Preferences...", None))
#if QT_CONFIG(shortcut)
        self.action_Preferences.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"&About...", None))
        self.action_Download_playlist_lite.setText(QCoreApplication.translate("MainWindow", u"Download playlist (lite)", None))
        self.action_Download_playlist_full.setText(QCoreApplication.translate("MainWindow", u"Download playlist (full)", None))
        self.action_Generate_playlist.setText(QCoreApplication.translate("MainWindow", u"Generate playlist...", None))
        self.action_Account_infos.setText(QCoreApplication.translate("MainWindow", u"Account infos", None))
        self.lbl_categories.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.date_start.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.chk_catchup.setText(QCoreApplication.translate("MainWindow", u"Catch up replay", None))
        self.lbl_catchup.setText(QCoreApplication.translate("MainWindow", u"No catchup available", None))
        self.lbl_channels.setText(QCoreApplication.translate("MainWindow", u"Channels", None))
        self.lbl_groups.setText(QCoreApplication.translate("MainWindow", u"Groups", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Live", None))
        self.lbl_channels_vod.setText(QCoreApplication.translate("MainWindow", u"Videos", None))
        self.lbl_groups_vod.setText(QCoreApplication.translate("MainWindow", u"Groups", None))
        self.picture_vod.setText("")
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"VOD", None))
        self.lbl_channels_series.setText(QCoreApplication.translate("MainWindow", u"Series", None))
        self.lbl_groups_series.setText(QCoreApplication.translate("MainWindow", u"Groups", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Series", None))
        self.btn_watch.setText(QCoreApplication.translate("MainWindow", u"Watch", None))
        self.lbl_wait.setText(QCoreApplication.translate("MainWindow", u"LOADING...", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_About.setTitle(QCoreApplication.translate("MainWindow", u"&?", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuXtream.setTitle(QCoreApplication.translate("MainWindow", u"Xtream", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

