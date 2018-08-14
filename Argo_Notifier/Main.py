# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui',
# licensing of 'Main.ui' applies.
#
# Created: Tue Aug 14 12:59:02 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_subject_name_Button = QtWidgets.QPushButton(self.centralwidget)
        self.open_subject_name_Button.setGeometry(QtCore.QRect(610, 510, 161, 31))
        self.open_subject_name_Button.setObjectName("open_subject_name_Button")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(610, 340, 160, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.status_argo_login = QtWidgets.QLabel(self.gridLayoutWidget)
        self.status_argo_login.setObjectName("status_argo_login")
        self.gridLayout.addWidget(self.status_argo_login, 0, 1, 1, 1)
        self.status_calendar_servers = QtWidgets.QLabel(self.gridLayoutWidget)
        self.status_calendar_servers.setObjectName("status_calendar_servers")
        self.gridLayout.addWidget(self.status_calendar_servers, 2, 1, 1, 1)
        self.status_calendar_login = QtWidgets.QLabel(self.gridLayoutWidget)
        self.status_calendar_login.setObjectName("status_calendar_login")
        self.gridLayout.addWidget(self.status_calendar_login, 1, 1, 1, 1)
        self.status_argo_servers = QtWidgets.QLabel(self.gridLayoutWidget)
        self.status_argo_servers.setObjectName("status_argo_servers")
        self.gridLayout.addWidget(self.status_argo_servers, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.open_settings_Button = QtWidgets.QPushButton(self.centralwidget)
        self.open_settings_Button.setGeometry(QtCore.QRect(610, 460, 161, 31))
        self.open_settings_Button.setObjectName("open_settings_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.open_subject_name_Button, QtCore.SIGNAL("clicked()"), MainWindow.open_subjects_window)
        QtCore.QObject.connect(self.open_settings_Button, QtCore.SIGNAL("clicked()"), MainWindow.open_settings_window)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.open_subject_name_Button.setText(QtWidgets.QApplication.translate("MainWindow", "Open subjects_window", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Argo_Login:", None, -1))
        self.status_argo_login.setText(QtWidgets.QApplication.translate("MainWindow", "none", None, -1))
        self.status_calendar_servers.setText(QtWidgets.QApplication.translate("MainWindow", "none", None, -1))
        self.status_calendar_login.setText(QtWidgets.QApplication.translate("MainWindow", "none", None, -1))
        self.status_argo_servers.setText(QtWidgets.QApplication.translate("MainWindow", "none", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Calendar_Login:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Calendar_Servers:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Argo_Servers", None, -1))
        self.open_settings_Button.setText(QtWidgets.QApplication.translate("MainWindow", "Open settings_window", None, -1))

