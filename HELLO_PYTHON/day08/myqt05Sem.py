import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("myqt05.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        
        self.pb_call.clicked.connect(self.callClick)
        
    def myclick(self):
        # 버튼이 클릭되었을 때 수행할 동작을 작성합니다.
        clicked_button = self.sender()
        button_text = clicked_button.text()
        current_text = self.le.text()
        self.le.setText(current_text + button_text)
        
    def callClick(self):
        txt = self.le.text()
        QMessageBox.about(self,'Call','Calling...'+txt)        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()