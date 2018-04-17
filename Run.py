# /usr/bin/env python3.4
# coding=utf-8

"""
    File_name  -> Run.py
    Author     -> Yu_dong
    Date       -> 2018/4/10
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import PLOFT

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = PLOFT.PLOFT()
    main.show()#在外面只需要调用simpleDialogForm显示就行，不需要关注内部如何实现了。
    sys.exit(app.exec_())