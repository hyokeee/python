import sys
from PyQt5 import QtWidgets, uic

class Form(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("myqt05.ui")  # UI 파일 불러오기
        self.ui.pb1.clicked.connect(self.click)  
        self.ui.pb2.clicked.connect(self.click)  
        self.ui.pb3.clicked.connect(self.click)  
        self.ui.pb4.clicked.connect(self.click)  
        self.ui.pb5.clicked.connect(self.click)  
        self.ui.pb6.clicked.connect(self.click)  
        self.ui.pb7.clicked.connect(self.click)  
        self.ui.pb8.clicked.connect(self.click)  
        self.ui.pb9.clicked.connect(self.click)  
        self.ui.pb0.clicked.connect(self.click)  
        self.ui.pb_call.clicked.connect(self.call)  # 버튼 클릭 이벤트 연결
        self.ui.show()

    def click(self):
        # 버튼이 클릭되었을 때 수행할 동작을 작성합니다.
        clicked_button = self.sender()
        button_text = clicked_button.text()
        current_text = self.ui.le.text()
        self.ui.le.setText(current_text + button_text)

    def call(self):
        
        phone_number = self.ui.le.text()
        # 전화를 걸기 위한 코드 작성
        message_box = QtWidgets.QMessageBox()
        message_box.setIcon(QtWidgets.QMessageBox.Information)
        message_box.setWindowTitle("전화 걸기")
        message_box.setText(f"전화를 거는 중입니다: {phone_number}")
        message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        message_box.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())