# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subject_table.ui',
# licensing of 'subject_table.ui' applies.
#
# Created: Sat Aug 11 17:10:11 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_subject_table(object):
    def setupUi(self, subject_table):
        subject_table.setObjectName("subject_table")
        subject_table.resize(747, 289)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(subject_table.sizePolicy().hasHeightForWidth())
        subject_table.setSizePolicy(sizePolicy)
        subject_table.setMinimumSize(QtCore.QSize(0, 0))
        subject_table.setBaseSize(QtCore.QSize(1500, 1500))
        subject_table.setWhatsThis("")
        self.gridLayout_3 = QtWidgets.QGridLayout(subject_table)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(subject_table)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(subject_table)
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

        self.retranslateUi(subject_table)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), subject_table.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), subject_table.reject)
        QtCore.QMetaObject.connectSlotsByName(subject_table)

    def retranslateUi(self, subject_table):
        subject_table.setWindowTitle(QtWidgets.QApplication.translate("subject_table", "Dialog", None, -1))
        self.tableWidget.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("subject_table", "1°", None, -1))
        self.tableWidget.verticalHeaderItem(1).setText(QtWidgets.QApplication.translate("subject_table", "2°", None, -1))
        self.tableWidget.verticalHeaderItem(2).setText(QtWidgets.QApplication.translate("subject_table", "3°", None, -1))
        self.tableWidget.verticalHeaderItem(3).setText(QtWidgets.QApplication.translate("subject_table", "4°", None, -1))
        self.tableWidget.verticalHeaderItem(4).setText(QtWidgets.QApplication.translate("subject_table", "5°", None, -1))
        self.tableWidget.verticalHeaderItem(5).setText(QtWidgets.QApplication.translate("subject_table", "6°", None, -1))
        self.tableWidget.verticalHeaderItem(6).setText(QtWidgets.QApplication.translate("subject_table", "7°", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("subject_table", "Lunedì", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("subject_table", "Martedì", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("subject_table", "Mecoledì", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("subject_table", "Giovedì", None, -1))
        self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("subject_table", "Venerdì", None, -1))
        self.tableWidget.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("subject_table", "Sabato", None, -1))
        self.tableWidget.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("subject_table", "Domenica", None, -1))

