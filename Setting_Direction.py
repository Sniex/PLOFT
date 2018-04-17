# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Setting_Direction.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(530, 290)
        self.Setting_Page = QtWidgets.QTabWidget(Form)
        self.Setting_Page.setGeometry(QtCore.QRect(0, -20, 531, 311))
        self.Setting_Page.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Current_Index = 0
        self.Next_Btn_Tab1 = QtWidgets.QPushButton(self.tab)
        self.Next_Btn_Tab1.setGeometry(QtCore.QRect(440, 260, 75, 23))
        self.Next_Btn_Tab1.setObjectName("Next_Btn_Tab1")
        self.Setting_Page.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Next_Btn_Tab2 = QtWidgets.QPushButton(self.tab_2)
        self.Next_Btn_Tab2.setGeometry(QtCore.QRect(440, 260, 75, 23))
        self.Next_Btn_Tab2.setObjectName("Next_Btn_Tab2")
        self.Last_Btn_Tab2 = QtWidgets.QPushButton(self.tab_2)
        self.Last_Btn_Tab2.setGeometry(QtCore.QRect(360, 260, 75, 23))
        self.Last_Btn_Tab2.setObjectName("Last_Btn_Tab2")
        self.Setting_Page.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.Finish_Btn_Tab3 = QtWidgets.QPushButton(self.tab_3)
        self.Finish_Btn_Tab3.setGeometry(QtCore.QRect(440, 260, 75, 23))
        self.Finish_Btn_Tab3.setObjectName("Finish_Btn_Tab3")

        self.Last_Btn_Tab3 = QtWidgets.QPushButton(self.tab_3)
        self.Last_Btn_Tab3.setGeometry(QtCore.QRect(360, 260, 75, 23))
        self.Last_Btn_Tab3.setObjectName("Last_Btn_Tab3")
        self.Setting_Page.addTab(self.tab_3, "")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(0, 0, 561, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        self.Setting_Page.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Next_Btn_Tab1.setText(_translate("Form", "下一页"))
        self.Setting_Page.setTabText(self.Setting_Page.indexOf(self.tab), _translate("Form", "1"))
        self.Next_Btn_Tab2.setText(_translate("Form", "下一页"))
        self.Last_Btn_Tab2.setText(_translate("Form", "上一页"))
        self.Setting_Page.setTabText(self.Setting_Page.indexOf(self.tab_2), _translate("Form", "2"))
        self.Last_Btn_Tab3.setText(_translate("Form", "上一页"))
        self.Finish_Btn_Tab3.setText(_translate("Form", "完成"))
        self.Setting_Page.setTabText(self.Setting_Page.indexOf(self.tab_3), _translate("Form", "3"))

    def mousePressEvent(self, event):
        # 定义鼠标点击事件
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        # 定义鼠标移动事件
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
