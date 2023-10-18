import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt07.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        a = int(self.le_first.text())
        b = int(self.le_last.text())
        star = ""
        for i in range(a,b+1):
            for _ in range(i):
                star += "*"
            star += "\n"
        self.te.setText(star)
        
    # def getStar(self,cnt):
    #     ret = ""
    #     for i in range(cnt):
    #         ret += "*"
    #     ret += "\n"
    #     return ret


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()