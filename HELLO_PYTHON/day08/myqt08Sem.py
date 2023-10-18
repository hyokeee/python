import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from random import random



form_class = uic.loadUiType("myqt08.ui")[0]


class WindowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.com =""
        self.pb.clicked.connect(self.btnClick)
        self.ranC()
        # le랑 Enter Key랑 Mapping
        self.le.returnPressed.connect(self.btnClick)
        
    def ranC(self):
        #1부터 9까지 배열 만들기
        arr = [];
        for i in range(1,9+1):
            arr.append(i)

        #배열 섞기
        for i in range(1,100+1):
            rnd = int(random()*9)
            a = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = a
    
        #com 숫자 만들기
        #self.com = str(arr[0])+str(arr[1])+str(arr[2])
        self.com = "{}{}{}".format(arr[0],arr[1],arr[2])
        
        
    def btnClick(self):
        print(self.com)
        mine = self.le.text()
        s = self.getStrike(self.com,mine)
        b = self.getBall(self.com, mine)
        str_new = mine + "\t" + str(s) + "S" + str(b) + "B\n"
        str_old = self.te.toPlainText()
        self.te.setText(str_new+str_old)
        self.le.setText("")
        
        if s == 3:
            QMessageBox.about(self,'야구게임','맞췄습니다!')
            app.exit()
    
    
    
    def getBall(self,com,mine):
        ret = 0
        c1 = com[0]
        c2 = com[1]
        c3 = com[2]
    
        m1 = mine[0]
        m2 = mine[1]
        m3 = mine[2]
    
        if c1 == m2 or c1 == m3:
            ret += 1
        if c2 == m1 or c2 == m3:
            ret += 1
        if c3 == m1 or c3 == m2:
            ret += 1
   
        return ret
    
    
       
    def getStrike(self,com,mine):
        ret = 0
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
    
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
    
        if c1 == m1:
            ret += 1
        if c2 == m2:
            ret += 1
        if c3 == m3:
            ret += 1
        return ret        
       
    def getCom(self):
        #1부터 9까지 배열 만들기
        arr = [];
        for i in range(1,9+1):
            arr.append(i)

        #배열 섞기
        for i in range(1,100+1):
            rnd = int(random()*9)
            a = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = a
    
        #com 숫자 만들기
        com = str(arr[0])+str(arr[1])+str(arr[2])
        return com


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
