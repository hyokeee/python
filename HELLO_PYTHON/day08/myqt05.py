import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("myqt05.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb0.clicked.connect(lambda: self.btnClick(self.pb0))
        self.pb1.clicked.connect(lambda: self.btnClick(self.pb1))
        self.pb2.clicked.connect(lambda: self.btnClick(self.pb2))
        self.pb3.clicked.connect(lambda: self.btnClick(self.pb3))
        self.pb4.clicked.connect(lambda: self.btnClick(self.pb4))
        self.pb5.clicked.connect(lambda: self.btnClick(self.pb5))
        self.pb6.clicked.connect(lambda: self.btnClick(self.pb6))
        self.pb7.clicked.connect(lambda: self.btnClick(self.pb7))
        self.pb8.clicked.connect(lambda: self.btnClick(self.pb8))
        self.pb9.clicked.connect(lambda: self.btnClick(self.pb9))
        
        # self.pb0.clicked.connect(partial(self.btnClick, self.pb0))
        # self.pb1.clicked.connect(partial(self.btnClick, self.pb1))
        # self.pb2.clicked.connect(partial(self.btnClick, self.pb2))
        # self.pb3.clicked.connect(partial(self.btnClick, self.pb3))
        # self.pb4.clicked.connect(partial(self.btnClick, self.pb4))
        # self.pb5.clicked.connect(partial(self.btnClick, self.pb5))
        # self.pb6.clicked.connect(partial(self.btnClick, self.pb6))
        # self.pb7.clicked.connect(partial(self.btnClick, self.pb7))
        # self.pb8.clicked.connect(partial(self.btnClick, self.pb8))
        # self.pb9.clicked.connect(partial(self.btnClick, self.pb9))
        
        self.pb_call.clicked.connect(self.callClick)
        
    def btnClick(self, button):
        b = button.text()
        str_old = self.le.text()
        str_new = b
        self.le.setText(str_old+str_new)
        
    def callClick(self):
        txt = self.le.text()
        QMessageBox.about(self,'Call','Calling...'+txt)        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()