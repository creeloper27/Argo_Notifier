# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SubjectsWindow.ui',
# licensing of 'SubjectsWindow.ui' applies.
#
# Created: Mon Oct 22 08:38:58 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SubjectsWindow(object):
    def setupUi(self, SubjectsWindow):
        SubjectsWindow.setObjectName("SubjectsWindow")
        SubjectsWindow.resize(747, 289)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SubjectsWindow.sizePolicy().hasHeightForWidth())
        SubjectsWindow.setSizePolicy(sizePolicy)
        SubjectsWindow.setMinimumSize(QtCore.QSize(0, 0))
        SubjectsWindow.setBaseSize(QtCore.QSize(0, 0))
        SubjectsWindow.setWhatsThis("")
        self.gridLayout_3 = QtWidgets.QGridLayout(SubjectsWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(SubjectsWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(SubjectsWindow)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(SubjectsWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SubjectsWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SubjectsWindow.reject)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("itemChanged(QTableWidgetItem*)"), SubjectsWindow.change_subject_table)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SubjectsWindow.update_subject_table)
        QtCore.QMetaObject.connectSlotsByName(SubjectsWindow)

    def retranslateUi(self, SubjectsWindow):
        SubjectsWindow.setWindowTitle(QtWidgets.QApplication.translate("SubjectsWindow", "Dialog", None, -1))
        self.tableWidget.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("SubjectsWindow", "1°", None, -1))
        self.tableWidget.verticalHeaderItem(1).setText(QtWidgets.QApplication.translate("SubjectsWindow", "2°", None, -1))
        self.tableWidget.verticalHeaderItem(2).setText(QtWidgets.QApplication.translate("SubjectsWindow", "3°", None, -1))
        self.tableWidget.verticalHeaderItem(3).setText(QtWidgets.QApplication.translate("SubjectsWindow", "4°", None, -1))
        self.tableWidget.verticalHeaderItem(4).setText(QtWidgets.QApplication.translate("SubjectsWindow", "5°", None, -1))
        self.tableWidget.verticalHeaderItem(5).setText(QtWidgets.QApplication.translate("SubjectsWindow", "6°", None, -1))
        self.tableWidget.verticalHeaderItem(6).setText(QtWidgets.QApplication.translate("SubjectsWindow", "7°", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("SubjectsWindow", "Lunedì", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("SubjectsWindow", "Martedì", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("SubjectsWindow", "Mecoledì", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("SubjectsWindow", "Giovedì", None, -1))
        self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("SubjectsWindow", "Venerdì", None, -1))
        self.tableWidget.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("SubjectsWindow", "Sabato", None, -1))
        self.tableWidget.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("SubjectsWindow", "Domenica", None, -1))

