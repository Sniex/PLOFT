# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Searching_Edit.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_Form(object):
    # def __init__(self):
    #     self.setWindowFlags(Qt.FramelessWindowHint)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(627, 72)
        self.Searching_Edit = QtWidgets.QLineEdit(Form)
        self.Searching_Edit.setGeometry(QtCore.QRect(0, 0, 540, 72))
        self.Searching_Edit.setStyleSheet("color:#bababa;\n"
"font: 22pt \"Consolas\";\n"
"background-color:#545454;\n"
"")
        self.Searching_Edit.setObjectName("Searching_Edit")
        self.Searching_Btn = QtWidgets.QPushButton(Form)
        self.Searching_Btn.setGeometry(QtCore.QRect(540, 0, 71, 72))
        self.Searching_Btn.setObjectName("Searching_Btn")
        self.Advance_Search_Btn = QtWidgets.QPushButton(Form)
        self.Advance_Search_Btn.setGeometry(QtCore.QRect(560, 0, 71, 72))
        self.Advance_Search_Btn.setObjectName("Advance_Search_Btn")
        self.Searching_Edit.raise_()
        self.Advance_Search_Btn.raise_()
        self.Searching_Btn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Searching_Btn.setText(_translate("Form", "Searching"))
        self.Advance_Search_Btn.setText(_translate("Form", "        ∨"))


