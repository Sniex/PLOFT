# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Float_Win.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import Float_Win_Qrc_rc

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(211, 73)
        # self.setWindowFlags(Qt.FramelessWindowHint)

        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(50, 0, 31, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMouseTracking(False)
        self.progressBar.setTabletTracking(False)
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(Form)
        self.progressBar_2.setEnabled(True)
        self.progressBar_2.setGeometry(QtCore.QRect(80, 0, 31, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy)
        self.progressBar_2.setMouseTracking(False)
        self.progressBar_2.setTabletTracking(False)
        self.progressBar_2.setAcceptDrops(False)
        self.progressBar_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_2.setAutoFillBackground(False)
        self.progressBar_2.setStyleSheet("#progress{\n"
"            width: 50%;\n"
"            height: 30px;\n"
"            border:1px solid #ccc;\n"
"            border-radius: 15px;\n"
"            margin: 50px 0 0 100px;\n"
"            overflow: hidden;\n"
"            box-shadow: 0 0 5px 0px #ddd inset;\n"
"        }\n"
"        ")
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setObjectName("progressBar_2")
        self.Switch_Btn = QtWidgets.QPushButton(Form)
        self.Switch_Btn.setGeometry(QtCore.QRect(0, 0, 50, 70))
        self.Switch_Btn.setStyleSheet("#Switch_Btn{\n"
"    border-image: url(:/Float_Win/image/left_Btn.png);\n"
"}\n"
"#Switch_Btn:hover{\n"
"    /*  */\n"
"}")
        self.Switch_Btn.setObjectName("Switch_Btn")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(110, -40, 101, 111))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Searching_Btn_2 = QtWidgets.QPushButton(self.tab)
        self.Searching_Btn_2.setGeometry(QtCore.QRect(0, 20, 101, 71))
        self.Searching_Btn_2.setObjectName("Searching_Btn_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.File_Arrange_Btn_2 = QtWidgets.QPushButton(self.tab_2)
        self.File_Arrange_Btn_2.setGeometry(QtCore.QRect(0, 20, 101, 71))
        self.File_Arrange_Btn_2.setObjectName("File_Arrange_Btn_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Switch_Btn.setText(_translate("Form", "Btn1"))
        self.Searching_Btn_2.setText(_translate("Form", "搜索框"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.File_Arrange_Btn_2.setText(_translate("Form", "文件整理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))



