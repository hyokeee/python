import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.Qt import QIcon, QSize


form_class = uic.loadUiType("omok02.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.turn = 0;
        for i in range(10):
            for j in range(10):  
                btn1 = QPushButton("",self)
                btn1.setGeometry(i*40,j*40,40,40)
                btn1.setIcon(QIcon("0.png"))
                btn1.setIconSize(QSize(40,40))
                    
                btn1.clicked.connect(self.btnClick)
        
        
        
    def btnClick(self): 
        btn = self.sender()
        print(btn.icon().name())
        if self.turn %2 == 0:
            btn.setIcon(QIcon('1.png'))
            self.turn += 1
        else:
            btn.setIcon(QIcon('2.png'))
            self.turn += 1
        
     


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()