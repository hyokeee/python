import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt06.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        mine = self.pte_mine.toPlainText()
        c = ["가위","바위","보"]
        rnd = int(random()*3)
        com = c[rnd]
        res = ""
        if mine == com:
            res = "비김"
        elif (mine,com) in [("가위","바위"),("바위","보"),("보","가위")]:
            res = "패배"
        elif (mine,com) in [("가위","보"),("바위","가위"),("보","바위")]:
            res = "승리"
        else:
            res = "잘못된 입력값"
        self.pte_com.setPlainText(com)
        self.pte_result.setPlainText(res)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()