# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Advance_Search.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(484, 620)
        Form.setStyleSheet("background-image: url(:/MainWindow/image/background.png);")
        self.Top_line = QtWidgets.QFrame(Form)
        self.Top_line.setGeometry(QtCore.QRect(0, 30, 481, 16))
        self.Top_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.Top_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Top_line.setObjectName("Top_line")
        self.Line_Mid_one = QtWidgets.QFrame(Form)
        self.Line_Mid_one.setGeometry(QtCore.QRect(0, 130, 481, 16))
        self.Line_Mid_one.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line_Mid_one.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line_Mid_one.setObjectName("Line_Mid_one")
        self.Line_Mid_two = QtWidgets.QFrame(Form)
        self.Line_Mid_two.setGeometry(QtCore.QRect(0, 270, 481, 16))
        self.Line_Mid_two.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line_Mid_two.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line_Mid_two.setObjectName("Line_Mid_two")
        self.Bottom_Line = QtWidgets.QFrame(Form)
        self.Bottom_Line.setGeometry(QtCore.QRect(0, 420, 481, 16))
        self.Bottom_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.Bottom_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Bottom_Line.setObjectName("Bottom_Line")
        self.File_name_type = QtWidgets.QLabel(Form)
        self.File_name_type.setGeometry(QtCore.QRect(10, 50, 54, 12))
        self.File_name_type.setObjectName("File_name_type")
        self.Fize_Size_type = QtWidgets.QLabel(Form)
        self.Fize_Size_type.setGeometry(QtCore.QRect(10, 150, 54, 12))
        self.Fize_Size_type.setObjectName("Fize_Size_type")
        self.File_Type_type = QtWidgets.QLabel(Form)
        self.File_Type_type.setGeometry(QtCore.QRect(10, 290, 54, 12))
        self.File_Type_type.setObjectName("File_Type_type")
        self.File_Create_type = QtWidgets.QLabel(Form)
        self.File_Create_type.setGeometry(QtCore.QRect(10, 440, 54, 12))
        self.File_Create_type.setObjectName("File_Create_type")
        self.File_Name_Search_Edit = QtWidgets.QLineEdit(Form)
        self.File_Name_Search_Edit.setGeometry(QtCore.QRect(110, 70, 271, 31))
        self.File_Name_Search_Edit.setObjectName("File_Name_Search_Edit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 170, 231, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Size_ceil = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Size_ceil.setObjectName("Size_ceil")
        self.horizontalLayout.addWidget(self.Size_ceil)
        self.Size_range = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Size_range.setObjectName("Size_range")
        self.horizontalLayout.addWidget(self.Size_range)
        self.Size_floor = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Size_floor.setObjectName("Size_floor")
        self.horizontalLayout.addWidget(self.Size_floor)
        self.File_Size_Unit = QtWidgets.QComboBox(Form)
        self.File_Size_Unit.setGeometry(QtCore.QRect(370, 200, 41, 22))
        self.File_Size_Unit.setObjectName("File_Size_Unit")
        self.File_Size_Unit.addItem("")
        self.File_Size_Unit.addItem("")
        self.File_Size_Unit.addItem("")
        self.File_Size_Unit.addItem("")
        self.File_Size_Unit.addItem("")
        self.File_Size_Unit.setItemText(4, "")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 300, 181, 114))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Type_ComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.Type_ComboBox.setObjectName("Type_ComboBox")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.Type_ComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.Type_ComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Type_Input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Type_Input.setObjectName("Type_Input")
        self.horizontalLayout_2.addWidget(self.Type_Input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 458, 415, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Year_Input_Floor = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Year_Input_Floor.setObjectName("Year_Input_Floor")
        self.horizontalLayout_4.addWidget(self.Year_Input_Floor)
        self.Year_Floor = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Year_Floor.setObjectName("Year_Floor")
        self.horizontalLayout_4.addWidget(self.Year_Floor)
        self.Month_Input_Floor = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Month_Input_Floor.setObjectName("Month_Input_Floor")
        self.horizontalLayout_4.addWidget(self.Month_Input_Floor)
        self.Month_Floor = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Month_Floor.setObjectName("Month_Floor")
        self.horizontalLayout_4.addWidget(self.Month_Floor)
        self.Day_Input_Floor = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Day_Input_Floor.setObjectName("Day_Input_Floor")
        self.horizontalLayout_4.addWidget(self.Day_Input_Floor)
        self.Day_Floor = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Day_Floor.setObjectName("Day_Floor")
        self.horizontalLayout_4.addWidget(self.Day_Floor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.File_Create_range = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.File_Create_range.setObjectName("File_Create_range")
        self.verticalLayout_2.addWidget(self.File_Create_range)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Year_Input_Ceil = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Year_Input_Ceil.setObjectName("Year_Input_Ceil")
        self.horizontalLayout_5.addWidget(self.Year_Input_Ceil)
        self.Year_Ceil = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Year_Ceil.setObjectName("Year_Ceil")
        self.horizontalLayout_5.addWidget(self.Year_Ceil)
        self.Month_Input_Ceil = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Month_Input_Ceil.setObjectName("Month_Input_Ceil")
        self.horizontalLayout_5.addWidget(self.Month_Input_Ceil)
        self.Month_Ceil = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Month_Ceil.setObjectName("Month_Ceil")
        self.horizontalLayout_5.addWidget(self.Month_Ceil)
        self.Day_Input_Ceil = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Day_Input_Ceil.setObjectName("Day_Input_Ceil")
        self.horizontalLayout_5.addWidget(self.Day_Input_Ceil)
        self.Day_Ceil = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Day_Ceil.setObjectName("Day_Ceil")
        self.horizontalLayout_5.addWidget(self.Day_Ceil)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.Search_Btn = QtWidgets.QPushButton(Form)
        self.Search_Btn.setGeometry(QtCore.QRect(205, 580, 80, 25))
        self.Search_Btn.setObjectName("Search_Btn")
        self.Exit_Btn = QtWidgets.QPushButton(Form)
        self.Exit_Btn.setGeometry(QtCore.QRect(450, 3, 30, 30))
        self.Exit_Btn.setStyleSheet("border-image: url(:/MainWindow/image/Close.png);")
        self.Exit_Btn.setText("")
        self.Exit_Btn.setObjectName("Exit_Btn")
        self.File_Check = QtWidgets.QCheckBox(Form)
        self.File_Check.setGeometry(QtCore.QRect(10, 80, 16, 16))
        self.File_Check.setText("")
        self.File_Check.setObjectName("File_Check")
        self.Size_Check = QtWidgets.QCheckBox(Form)
        self.Size_Check.setGeometry(QtCore.QRect(10, 210, 16, 16))
        self.Size_Check.setText("")
        self.Size_Check.setObjectName("Size_Check")
        self.Type_Check = QtWidgets.QCheckBox(Form)
        self.Type_Check.setGeometry(QtCore.QRect(10, 340, 16, 16))
        self.Type_Check.setText("")
        self.Type_Check.setObjectName("Type_Check")
        self.Create_Check = QtWidgets.QCheckBox(Form)
        self.Create_Check.setGeometry(QtCore.QRect(10, 500, 16, 16))
        self.Create_Check.setText("")
        self.Create_Check.setObjectName("Create_Check")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.File_name_type.setText(_translate("Form", "文件名称："))
        self.Fize_Size_type.setText(_translate("Form", "文件大小："))
        self.File_Type_type.setText(_translate("Form", "文件类型"))
        self.File_Create_type.setText(_translate("Form", "创建时间："))
        self.Size_range.setText(_translate("Form", "—"))
        self.File_Size_Unit.setItemText(0, _translate("Form", "B"))
        self.File_Size_Unit.setItemText(1, _translate("Form", "KB"))
        self.File_Size_Unit.setItemText(2, _translate("Form", "MB"))
        self.File_Size_Unit.setItemText(3, _translate("Form", "GB"))
        self.Type_ComboBox.setItemText(0, _translate("Form", "mpg"))
        self.Type_ComboBox.setItemText(1, _translate("Form", "mpeg"))
        self.Type_ComboBox.setItemText(2, _translate("Form", "avi"))
        self.Type_ComboBox.setItemText(3, _translate("Form", "rm"))
        self.Type_ComboBox.setItemText(4, _translate("Form", "rmvb"))
        self.Type_ComboBox.setItemText(5, _translate("Form", "mov"))
        self.Type_ComboBox.setItemText(6, _translate("Form", "wmv"))
        self.Type_ComboBox.setItemText(7, _translate("Form", "asf"))
        self.Type_ComboBox.setItemText(8, _translate("Form", "dat"))
        self.Type_ComboBox.setItemText(9, _translate("Form", "mp4"))
        self.Type_ComboBox.setItemText(10, _translate("Form", "mp3"))
        self.Type_ComboBox.setItemText(11, _translate("Form", "wma"))
        self.Type_ComboBox.setItemText(12, _translate("Form", "ram"))
        self.Type_ComboBox.setItemText(13, _translate("Form", "wav"))
        self.Type_ComboBox.setItemText(14, _translate("Form", "mid"))
        self.Type_ComboBox.setItemText(15, _translate("Form", "midi"))
        self.Type_ComboBox.setItemText(16, _translate("Form", "rmi"))
        self.Type_ComboBox.setItemText(17, _translate("Form", "m3u"))
        self.Type_ComboBox.setItemText(18, _translate("Form", "wpl"))
        self.Type_ComboBox.setItemText(19, _translate("Form", "ogg"))
        self.Type_ComboBox.setItemText(20, _translate("Form", "ape"))
        self.Type_ComboBox.setItemText(21, _translate("Form", "cda"))
        self.Type_ComboBox.setItemText(22, _translate("Form", "exe"))
        self.Type_ComboBox.setItemText(23, _translate("Form", "msi"))
        self.Type_ComboBox.setItemText(24, _translate("Form", "bat"))
        self.Type_ComboBox.setItemText(25, _translate("Form", "txt"))
        self.Type_ComboBox.setItemText(26, _translate("Form", "rtf"))
        self.Type_ComboBox.setItemText(27, _translate("Form", "htm"))
        self.Type_ComboBox.setItemText(28, _translate("Form", "html"))
        self.Type_ComboBox.setItemText(29, _translate("Form", "mht"))
        self.Type_ComboBox.setItemText(30, _translate("Form", "doc"))
        self.Type_ComboBox.setItemText(31, _translate("Form", "docx"))
        self.Type_ComboBox.setItemText(32, _translate("Form", "ppt"))
        self.Type_ComboBox.setItemText(33, _translate("Form", "pptx"))
        self.Type_ComboBox.setItemText(34, _translate("Form", "vsd"))
        self.Type_ComboBox.setItemText(35, _translate("Form", "lnk"))
        self.Type_ComboBox.setItemText(36, _translate("Form", "chm"))
        self.Type_ComboBox.setItemText(37, _translate("Form", "reg"))
        self.Type_ComboBox.setItemText(38, _translate("Form", "dll"))
        self.Type_ComboBox.setItemText(39, _translate("Form", "ini"))
        self.Type_ComboBox.setItemText(40, _translate("Form", "log"))
        self.Type_ComboBox.setItemText(41, _translate("Form", "fla"))
        self.Type_ComboBox.setItemText(42, _translate("Form", "swf"))
        self.Type_ComboBox.setItemText(43, _translate("Form", "xls"))
        self.Type_ComboBox.setItemText(44, _translate("Form", "xlsx"))
        self.Type_ComboBox.setItemText(45, _translate("Form", "zip"))
        self.Type_ComboBox.setItemText(46, _translate("Form", "rar"))
        self.Type_ComboBox.setItemText(47, _translate("Form", "cab"))
        self.Type_ComboBox.setItemText(48, _translate("Form", "ace"))
        self.Type_ComboBox.setItemText(49, _translate("Form", "z"))
        self.Type_ComboBox.setItemText(50, _translate("Form", "arc"))
        self.Type_ComboBox.setItemText(51, _translate("Form", "tar"))
        self.Type_ComboBox.setItemText(52, _translate("Form", "7z"))
        self.Type_ComboBox.setItemText(53, _translate("Form", "gz"))
        self.Type_ComboBox.setItemText(54, _translate("Form", "jpg"))
        self.Type_ComboBox.setItemText(55, _translate("Form", "jpeg"))
        self.Type_ComboBox.setItemText(56, _translate("Form", "gif"))
        self.Type_ComboBox.setItemText(57, _translate("Form", "bmp"))
        self.Type_ComboBox.setItemText(58, _translate("Form", "png"))
        self.Type_ComboBox.setItemText(59, _translate("Form", "ico"))
        self.Type_ComboBox.setItemText(60, _translate("Form", "psd"))
        self.Type_ComboBox.setItemText(61, _translate("Form", "tif"))
        self.Year_Floor.setText(_translate("Form", "年"))
        self.Month_Floor.setText(_translate("Form", "月"))
        self.Day_Floor.setText(_translate("Form", "日"))
        self.File_Create_range.setText(_translate("Form", "                                 至"))
        self.Year_Ceil.setText(_translate("Form", "年"))
        self.Month_Ceil.setText(_translate("Form", "月"))
        self.Day_Ceil.setText(_translate("Form", "日"))
        self.Search_Btn.setText(_translate("Form", "搜索"))

import Float_Win_Qrc_rc