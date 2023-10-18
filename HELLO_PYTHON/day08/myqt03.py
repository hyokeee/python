import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt03.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        lotto = [i+1 for i in range(45)]
        
        for i in range(100):
            rnd = int(random()*45)
            temp = lotto[0]
            lotto[0] = lotto[rnd]
            lotto[rnd] = temp
            
        lottolist = sorted(lotto[:6])
        self.lbl1.setText(str(lottolist[0]))
        self.lbl2.setText(str(lottolist[1]))
        self.lbl3.setText(str(lottolist[2]))
        self.lbl4.setText(str(lottolist[3]))
        self.lbl5.setText(str(lottolist[4]))
        self.lbl6.setText(str(lottolist[5]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()