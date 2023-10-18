import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("omok01.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lbl.mousePressEvent = self.btnClick
        self.pb.mousePressEvent = self.btnClick
    def btnClick(self,event):
        self.lbl.setPixmap(QtGui.QPixmap('1.png'))
        self.pb.setIcon(QtGui.QIcon('1.png'))
        
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()