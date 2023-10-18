import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from random import random
from _functools import partial


form_class = uic.loadUiType("myqt08.ui")[0]


class WindowClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        com1 = self.getCom();
        self.pb.clicked.connect(partial(self.btnClick,com1))
        
        
        
    def btnClick(self, com1):
        print(com1)     
        mine = self.le.text() 
        strike = self.getStrike(com1, mine)
        ball = self.getBall(com1, mine)
        old = self.te.toPlainText()
        res =""
        if strike == 3:
            res = mine + "\t정답입니다.\n"
            QMessageBox.about(self,'정답',res)
        else:
            res = mine+"\t"+str(strike)+"S"+str(ball)+"B\n"
            
        self.te.setText(res+old)
        self.le.setText("")
    
    
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
        c1 = com[0]
        c2 = com[1]
        c3 = com[2]
    
        m1 = mine[0]
        m2 = mine[1]
        m3 = mine[2]
    
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
