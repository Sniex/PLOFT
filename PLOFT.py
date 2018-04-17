# /usr/bin/env python3.4
# coding=utf-8

"""
    File_name  -> PLOFT.py
    Author     -> Yu_dong
    Date       -> 2018/4/10
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, QMenu, QSystemTrayIcon, QApplication
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QIcon

import PLOFT_Main_Win, Float_Win, Setting_Direction, Searching_Edit, Close_Dialog, Advance_Search


class PLOFT(PLOFT_Main_Win.Ui_MainWindow, QtWidgets.QWidget):

    isVisible_float_win = 0
    isVisible_search_win = 0

    def __init__(self, parent = None):
        super(PLOFT, self).__init__()
        self.setupUi(self)#在此设置界面
        self.close_type = -1

        #在此，可添加自定义的信号绑定
        self.float_win = Float_win(self)
        # self.float_win = None
        self.Float_Win_Btn.clicked.connect(self.Float_win)

        self.setting_win = Setting_win()
        # self.setting_win = None
        self.Setting_Btn.clicked.connect(self.Setting_Btn_Clicked)


        self.searching_win = Searching_win()
        self.Searching_Btn.clicked.connect(self.Searching_Btn_Clicked)


        self.close_dialog = None
        self.Exit_Btn.clicked.connect(self.Exit_Btn_Clicked)

        self.Advance_Search = Advance_Search_win()


        # 窗口无边框化，写于QMainwindow所在子类初始化函数中
        self.setWindowFlags(Qt.FramelessWindowHint)     # 去边框
        # self.setWindowFlags(Qt.SplashScreen)

        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        # 窗口背景透明

    def Show_All(self):
        self.show()
        if PLOFT.isVisible_float_win == 1:
            self.float_win.close()
            self.float_win.show()

    def Float_win(self):
        # if self.float_win is not None:
        #     print("\\\\")
        PLOFT.isVisible_float_win = 1
        self.float_win.show()

    def Searching_Btn_Clicked(self):
        # self.searching_win = Searching_Edit.Ui_Form()
        # self.Widget2 = QtWidgets.QMainWindow()
        #
        # self.searching_win.setupUi(self.Widget2)
        #
        # # 子窗口信号槽：
        # self.searching_win.Searching_Btn_2.clicked.connect(self.Advance_Search_Clicked)
        # # 去边框
        # self.Widget2.setWindowFlag(Qt.SplashScreen)
        #
        # PLOFT.isVisible_search_win = 1
        #
        # self.Widget2.show()

        PLOFT.isVisible_search_win = 1
        self.searching_win.show()

    def Setting_Btn_Clicked(self):
        # self.setting_win = Setting_Direction.Ui_Form()


        self.setting_win.show()

    def Exit_Btn_Clicked(self):
        # self.hide()
        if self.close_type == 0:
            self.addSystemTray()
        elif self.close_type == 1:
            self.Widget3.close()
            self.close()
        else:
            self.close_dialog = Close_Dialog.Ui_Dialog()
            self.Widget3 = QtWidgets.QDialog()

            self.close_dialog.setupUi(self.Widget3)
            self.Widget3.setWindowFlags(Qt.SplashScreen)

            self.close_dialog.Comfirm_Btn.clicked.connect(self.Close_Event)
            self.close_dialog.Close_Btn.clicked.connect(self.Widget3.close)
            # 去边框
            # self.Widget3.setWindowFlag(Qt.SplashScreen)
            self.Widget3.show()

    def addSystemTray(self):
        self.tray = QSystemTrayIcon()  # 创建系统托盘对象
        self.icon = QIcon('res/image/close.png')  # 创建图标
        self.tray.setIcon(self.icon)  # 设置系统托盘图标

        self.tray_menu = QMenu(QApplication.desktop())  # 创建菜单
        self.RestoreAction = QAction(u'还原 ', self, triggered=self.Show_All)  # 添加一级菜单动作选项(还原主窗口)
        self.QuitAction = QAction(u'退出 ', self, triggered=self.close)  # 添加一级菜单动作选项(退出程序)

        self.tray_menu.addAction(self.RestoreAction)  # 为菜单添加动作
        self.tray_menu.addAction(self.QuitAction)
        self.tray.setContextMenu(self.tray_menu)  # 设置系统托盘菜单
        self.hide()
        self.tray.show()

    def Close_Event(self):
        if self.close_dialog.Exit_To_Ploft.isChecked() or self.close_type == 1:
            if self.close_dialog.No_Repeat.isChecked():
                self.close_type = 1
            self.Widget3.close()
            self.close()

        elif self.close_dialog.Mini_To_Tray.isChecked() or self.close_type == 0:
            if self.close_dialog.No_Repeat.isChecked():
                self.close_type = 0
            self.addSystemTray()
            self.Widget3.close()
            if PLOFT.isVisible_float_win == 1:
                self.float_win.close()
                self.float_win.show()
            if PLOFT.isVisible_search_win == 1:
                self.searching_win.close()
                self.searching_win.show()


    def mousePressEvent(self, event):
        # 定义鼠标点击事件
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
        if event.buttons() == QtCore.Qt.MiddleButton:
            self.mousePosition = event.screenPos().x() * event.screenPos().x() + event.screenPos().y() * event.screenPos().y()
            print(self.mousePosition)
            event.accept()

    def keyPressEvent(self, event):
        if ( Qt.Key_Control | Qt.Key_Shift ) and event.key() == Qt.Key_Z:
            print("::::::")
            if PLOFT.isVisible_search_win == 0:
                print("6666")
                self.searching_win.show()
                event.accept()



    def mouseMoveEvent(self, event):
        # 定义鼠标移动事件
        if event.buttons() == QtCore.Qt.LeftButton:
            # print(type(event.buttons()))
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
        # print("-----", PLOFT.isVisible_search_win)
        if event.buttons() == QtCore.Qt.MidButton and PLOFT.isVisible_search_win == 0:
            nowPos = event.screenPos().x() * event.screenPos().x() + event.screenPos().y() * event.screenPos().y()
            if nowPos - self.mousePosition > self.mousePosition / 5:

                self.searching_win.show()
                event.accept()

class Float_win(Float_Win.Ui_Form, QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(Float_win, self).__init__()
        self.setWindowFlag(Qt.SplashScreen)
        self.setupUi(self)

    def closeEvent(self, event):
        PLOFT.isVisible_float_win = 0
        event.accept()

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

    def contextMenuEvent(self, QContextMenuEvent):
        self._float_menu = QMenu(self)
        self._float_menu.addAction(QAction(u'退出 ', self, triggered = self.close)) # 添加一级菜单动作选项(退出程序)
        self._float_menu.move(self.cursor().pos())
        self._float_menu.show()

class Searching_win(Searching_Edit.Ui_Form, QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(Searching_win, self).__init__()
        self.setWindowFlag(Qt.SplashScreen)
        self.setupUi(self)

        self.Advance_Search = Advance_Search_win()

        self.Advance_Search_Btn.clicked.connect(self.Advance_Search_Clicked)

    def Advance_Search_Clicked(self):
        self.Advance_Search.show()

    def closeEvent(self, event):
        PLOFT.isVisible_search_win = 0
        event.accept()

    def mousePressEvent(self, event):
        # 定义鼠标点击事件
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        # 定义鼠标移动事件

        if event.buttons() == QtCore.Qt.LeftButton:
            print("++++")
            self.move(event.globalPos() - self.dragPosition)

            event.accept()


    def contextMenuEvent(self, QContextMenuEvent):
        self._search_menu = QMenu(self)
        self._search_menu.addAction(QAction(u'退出 ', self, triggered = self.close)) # 添加一级菜单动作选项(退出程序)
        self._search_menu.move(self.cursor().pos())
        self._search_menu.show()

class Close_win(Close_Dialog.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(Close_win, self).__init__()
        self.setupUi(self)

        self.Comfirm_Btn.clicked.connect(self.Close_Event)

    def Close_Event(self):
        if self.Exit_To_Ploft.isChecked():
            self.close()

class Setting_win(Setting_Direction.Ui_Form, QtWidgets.QDialog):

    def __init__(self, parent = None):
        super(Setting_win, self).__init__()
        self.setWindowFlags(Qt.SplashScreen) # 去边框
        self.setupUi(self)

        self.Next_Btn_Tab1.clicked.connect(self.Next_Page_Tab)
        self.Next_Btn_Tab2.clicked.connect(self.Next_Page_Tab)
        self.Last_Btn_Tab2.clicked.connect(self.Last_Page_Tab)
        self.Last_Btn_Tab3.clicked.connect(self.Last_Page_Tab)
        self.Finish_Btn_Tab3.clicked.connect(self.Finish_Page_Tab3)

    def Next_Page_Tab(self):
        self.Current_Index += 1
        self.Setting_Page.setCurrentIndex(self.Current_Index)

    def Last_Page_Tab(self):
        self.Current_Index -= 1
        self.Setting_Page.setCurrentIndex(self.Current_Index)

    def Finish_Page_Tab3(self):
        """
        设置业务完成逻辑
        """
        self.Current_Index = 0
        self.Setting_Page.setCurrentIndex(self.Current_Index)
        self.close()

class Advance_Search_win(Advance_Search.Ui_Form, QtWidgets.QWidget):

    def __init__(self, parent = None):
        super(Advance_Search_win, self).__init__()
        self.setWindowFlags(Qt.SplashScreen) # 去边框
        self.setupUi(self)

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

