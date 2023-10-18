import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt04.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        dan = self.le.text()
        ddan = int(dan)
        txt = "*****"+dan+"단*****\n"
        for i in range(1,9+1):
            txt += dan + " * " + str(i) + " = " + str(ddan*i) + "\n"
        
        self.te.setText(txt)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()