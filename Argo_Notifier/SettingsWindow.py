# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsWindow.ui',
# licensing of 'SettingsWindow.ui' applies.
#
# Created: Fri Sep 14 13:09:36 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsWindow)
        self.buttonBox.setGeometry(QtCore.QRect(230, 260, 156, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.auto_update_interval_spinBox = QtWidgets.QSpinBox(SettingsWindow)
        self.auto_update_interval_spinBox.setGeometry(QtCore.QRect(180, 100, 42, 22))
        self.auto_update_interval_spinBox.setObjectName("auto_update_interval_spinBox")
        self.label = QtWidgets.QLabel(SettingsWindow)
        self.label.setGeometry(QtCore.QRect(60, 100, 111, 20))
        self.label.setObjectName("label")
        self.start_on_startup_checkBox = QtWidgets.QCheckBox(SettingsWindow)
        self.start_on_startup_checkBox.setGeometry(QtCore.QRect(180, 140, 16, 17))
        self.start_on_startup_checkBox.setText("")
        self.start_on_startup_checkBox.setObjectName("start_on_startup_checkBox")
        self.label_2 = QtWidgets.QLabel(SettingsWindow)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 91, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(SettingsWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SettingsWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SettingsWindow.reject)
        QtCore.QObject.connect(self.auto_update_interval_spinBox, QtCore.SIGNAL("valueChanged(int)"), SettingsWindow.change_settings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SettingsWindow.update_settings)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QtWidgets.QApplication.translate("SettingsWindow", "Dialog", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("SettingsWindow", "auto_update_interval", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("SettingsWindow", "start_on_startup", None, -1))

