# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Close_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Float_Win_Qrc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 214)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Comfirm_Btn = QtWidgets.QPushButton(Dialog)
        self.Comfirm_Btn.setGeometry(QtCore.QRect(310, 180, 75, 23))
        self.Comfirm_Btn.setObjectName("Comfirm_Btn")
        self.Top_Line = QtWidgets.QFrame(Dialog)
        self.Top_Line.setGeometry(QtCore.QRect(0, 30, 411, 16))
        self.Top_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.Top_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Top_Line.setObjectName("Top_Line")
        self.Close_Tips = QtWidgets.QLabel(Dialog)
        self.Close_Tips.setGeometry(QtCore.QRect(10, 5, 111, 31))
        self.Close_Tips.setStyleSheet("font: 20pt \"华文行楷\";")
        self.Close_Tips.setObjectName("Close_Tips")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 60, 141, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Mini_To_Tray = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Mini_To_Tray.setObjectName("Mini_To_Tray")
        self.verticalLayout.addWidget(self.Mini_To_Tray)
        self.Exit_To_Ploft = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Exit_To_Ploft.setObjectName("Exit_To_Ploft")
        self.verticalLayout.addWidget(self.Exit_To_Ploft)
        self.Bottom_Line = QtWidgets.QFrame(Dialog)
        self.Bottom_Line.setGeometry(QtCore.QRect(0, 160, 411, 16))
        self.Bottom_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.Bottom_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Bottom_Line.setObjectName("Bottom_Line")
        self.No_Repeat = QtWidgets.QCheckBox(Dialog)
        self.No_Repeat.setGeometry(QtCore.QRect(20, 180, 71, 16))
        self.No_Repeat.setObjectName("No_Repeat")
        self.Close_Btn = QtWidgets.QPushButton(Dialog)
        self.Close_Btn.setGeometry(QtCore.QRect(375, 5, 20, 20))
        self.Close_Btn.setStyleSheet("border-image: url('res/image/Close.png');")
        self.Close_Btn.setText("")
        self.Close_Btn.setObjectName("Close_Btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Comfirm_Btn.setText(_translate("Dialog", "确定"))
        self.Close_Tips.setText(_translate("Dialog", "关闭提示"))
        self.Mini_To_Tray.setText(_translate("Dialog", "最小化到系统托盘"))
        self.Exit_To_Ploft.setText(_translate("Dialog", "退出PLOFT"))
        self.No_Repeat.setText(_translate("Dialog", "不再提醒"))


