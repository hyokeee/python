import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt01.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        a = self.lbl.text()
        if a == "Good Morning":
            self.lbl.setText("Good Afternoon")
        elif a == "Good Afternoon":
            self.lbl.setText("Good Evening")
        else:
            self.lbl.setText("Good Morning")
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()