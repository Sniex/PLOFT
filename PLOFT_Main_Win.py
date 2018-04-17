# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PLOFT_Main_Win.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 600)
        MainWindow.setStyleSheet("background-image: url(:/MainWindow/image/background.png);")
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 440, 320, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.File_Arrange_Btn = QtWidgets.QPushButton(self.layoutWidget)
        self.File_Arrange_Btn.setObjectName("File_Arrange_Btn")
        self.gridLayout.addWidget(self.File_Arrange_Btn, 0, 2, 1, 1)
        self.Searching_Btn = QtWidgets.QPushButton(self.layoutWidget)
        self.Searching_Btn.setObjectName("Searching_Btn")
        self.gridLayout.addWidget(self.Searching_Btn, 0, 3, 1, 1)
        self.Float_Win_Btn = QtWidgets.QPushButton(self.layoutWidget)
        self.Float_Win_Btn.setObjectName("Float_Win_Btn")
        self.gridLayout.addWidget(self.Float_Win_Btn, 0, 0, 1, 1)
        self.Setting_Btn = QtWidgets.QPushButton(self.layoutWidget)
        self.Setting_Btn.setObjectName("Setting_Btn")
        self.gridLayout.addWidget(self.Setting_Btn, 0, 1, 1, 1)
        self.Exit_Btn = QtWidgets.QPushButton(MainWindow)
        self.Exit_Btn.setGeometry(QtCore.QRect(420, 0, 30, 30))
        self.Exit_Btn.setStyleSheet("border-image: url('res/image/Close.png');")
        self.Exit_Btn.setText("")
        self.Exit_Btn.setObjectName("Exit_Btn")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.File_Arrange_Btn.setText(_translate("MainWindow", "文件整理"))
        self.Searching_Btn.setText(_translate("MainWindow", "搜索框"))
        self.Float_Win_Btn.setText(_translate("MainWindow", "悬浮窗"))
        self.Setting_Btn.setText(_translate("MainWindow", "设置"))

import Float_Win_Qrc_rc
