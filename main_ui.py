# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 672)
        MainWindow.setMinimumSize(QtCore.QSize(700, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../resources/play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list_categ_1 = QtWidgets.QListWidget(self.centralwidget)
        self.list_categ_1.setGeometry(QtCore.QRect(10, 40, 256, 421))
        self.list_categ_1.setObjectName("list_categ_1")
        self.list_categ_2 = QtWidgets.QListWidget(self.centralwidget)
        self.list_categ_2.setGeometry(QtCore.QRect(290, 40, 256, 421))
        self.list_categ_2.setObjectName("list_categ_2")
        self.list_channels = QtWidgets.QListWidget(self.centralwidget)
        self.list_channels.setGeometry(QtCore.QRect(570, 40, 256, 421))
        self.list_channels.setObjectName("list_channels")
        self.btn_watch = QtWidgets.QPushButton(self.centralwidget)
        self.btn_watch.setGeometry(QtCore.QRect(730, 470, 93, 28))
        self.btn_watch.setObjectName("btn_watch")
        self.lbl_groups = QtWidgets.QLabel(self.centralwidget)
        self.lbl_groups.setGeometry(QtCore.QRect(10, 15, 121, 16))
        self.lbl_groups.setObjectName("lbl_groups")
        self.lbl_categories = QtWidgets.QLabel(self.centralwidget)
        self.lbl_categories.setGeometry(QtCore.QRect(290, 15, 121, 16))
        self.lbl_categories.setObjectName("lbl_categories")
        self.lbl_channels = QtWidgets.QLabel(self.centralwidget)
        self.lbl_channels.setGeometry(QtCore.QRect(570, 15, 121, 16))
        self.lbl_channels.setObjectName("lbl_channels")
        self.lbl_wait = QtWidgets.QLabel(self.centralwidget)
        self.lbl_wait.setGeometry(QtCore.QRect(270, 140, 301, 241))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lbl_wait.setFont(font)
        self.lbl_wait.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_wait.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_wait.setObjectName("lbl_wait")
        self.txt_filter_groups = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_filter_groups.setGeometry(QtCore.QRect(120, 10, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txt_filter_groups.setFont(font)
        self.txt_filter_groups.setObjectName("txt_filter_groups")
        self.txt_filter_categories = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_filter_categories.setGeometry(QtCore.QRect(402, 10, 141, 25))
        self.txt_filter_categories.setObjectName("txt_filter_categories")
        self.txt_filter_channels = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_filter_channels.setGeometry(QtCore.QRect(682, 10, 141, 25))
        self.txt_filter_channels.setObjectName("txt_filter_channels")
        self.txt_url = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_url.setEnabled(True)
        self.txt_url.setGeometry(QtCore.QRect(10, 470, 711, 25))
        self.txt_url.setReadOnly(True)
        self.txt_url.setObjectName("txt_url")
        self.frm_catchup = QtWidgets.QFrame(self.centralwidget)
        self.frm_catchup.setGeometry(QtCore.QRect(10, 510, 821, 51))
        self.frm_catchup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_catchup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_catchup.setObjectName("frm_catchup")
        self.time_start = QtWidgets.QTimeEdit(self.frm_catchup)
        self.time_start.setGeometry(QtCore.QRect(250, 0, 71, 22))
        self.time_start.setObjectName("time_start")
        self.chk_catchup = QtWidgets.QCheckBox(self.frm_catchup)
        self.chk_catchup.setGeometry(QtCore.QRect(0, 0, 121, 20))
        self.chk_catchup.setObjectName("chk_catchup")
        self.date_start = QtWidgets.QDateEdit(self.frm_catchup)
        self.date_start.setGeometry(QtCore.QRect(130, 0, 110, 22))
        self.date_start.setObjectName("date_start")
        self.lbl_catchup = QtWidgets.QLabel(self.frm_catchup)
        self.lbl_catchup.setGeometry(QtCore.QRect(0, 30, 311, 16))
        self.lbl_catchup.setObjectName("lbl_catchup")
        self.cmb_epg = QtWidgets.QComboBox(self.frm_catchup)
        self.cmb_epg.setGeometry(QtCore.QRect(410, 0, 401, 22))
        self.cmb_epg.setObjectName("cmb_epg")
        self.txt_duration = QtWidgets.QLineEdit(self.frm_catchup)
        self.txt_duration.setGeometry(QtCore.QRect(330, 0, 51, 22))
        self.txt_duration.setObjectName("txt_duration")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 26))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_About = QtWidgets.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_api = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\../resources/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_api.setIcon(icon1)
        self.action_api.setObjectName("action_api")
        self.action_Open_local_file = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui\\../resources/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open_local_file.setIcon(icon2)
        self.action_Open_local_file.setObjectName("action_Open_local_file")
        self.action_Open_remote_file = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui\\../resources/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open_remote_file.setIcon(icon3)
        self.action_Open_remote_file.setObjectName("action_Open_remote_file")
        self.action_Preferences = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui\\../resources/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Preferences.setIcon(icon4)
        self.action_Preferences.setObjectName("action_Preferences")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.menu_File.addAction(self.action_api)
        self.menu_File.addAction(self.action_Open_local_file)
        self.menu_File.addAction(self.action_Open_remote_file)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Preferences)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_About.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.toolBar.addAction(self.action_api)
        self.toolBar.addAction(self.action_Open_local_file)
        self.toolBar.addAction(self.action_Open_remote_file)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Preferences)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Playlist Browser"))
        self.btn_watch.setText(_translate("MainWindow", "Watch"))
        self.lbl_groups.setText(_translate("MainWindow", "Groups"))
        self.lbl_categories.setText(_translate("MainWindow", "Categories"))
        self.lbl_channels.setText(_translate("MainWindow", "Channels"))
        self.lbl_wait.setText(_translate("MainWindow", "LOADING..."))
        self.chk_catchup.setText(_translate("MainWindow", "Catch up replay"))
        self.date_start.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.lbl_catchup.setText(_translate("MainWindow", "No catchup available"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_About.setTitle(_translate("MainWindow", "&?"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_api.setText(_translate("MainWindow", "&Xstream Code API..."))
        self.action_Open_local_file.setText(_translate("MainWindow", "&Open local file..."))
        self.action_Open_local_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_Open_remote_file.setText(_translate("MainWindow", "Open &remote file..."))
        self.action_Open_remote_file.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_Preferences.setText(_translate("MainWindow", "&Preferences..."))
        self.action_Preferences.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_Exit.setText(_translate("MainWindow", "E&xit"))
        self.action_About.setText(_translate("MainWindow", "&About..."))
