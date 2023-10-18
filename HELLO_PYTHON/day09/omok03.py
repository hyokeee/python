import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.Qt import QIcon, QSize


form_class = uic.loadUiType("omok03.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
        self.pb2D = []
        self.turn = 0
        self.back2D = []
        self.flag_over = False
        for i in range(10):
            line = []
            for j in range(10):  
                btn1 = QPushButton("",self)
                btn1.setGeometry(j*40,i*40,40,40)
                btn1.setIcon(QIcon("0.png"))
                btn1.setToolTip("{},{}".format(i,j))
                btn1.setIconSize(QSize(40,40))            
                btn1.clicked.connect(self.btnClick)
                line.append(btn1)
            self.pb2D.append(line)    
        
        
        self.pb_back.clicked.connect(self.back) 
        self.pb.clicked.connect(self.my_reset)
        self.myrender()
        
    def my_reset(self):   
        self.flag_over = False
        self.turn = 0
        for i in range(10):
            for j in range(10):
                self.arr2D[i][j] = 0
        self.myrender()
        
    def checkUP(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -=1
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt+=1
                else:
                    return cnt
        except:
            return cnt
            
    def checkDown(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
              
                # if i>len(self.arr2D)-1:
                #     return cnt  
                if self.arr2D[i][j] == stone:
                    cnt +=1
                else:
                    return cnt
        except:
            return cnt
        
    def checkRight(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += 1
                if self.arr2D[i][j] == stone:
                    cnt +=1
                else:
                    return cnt
        except:
            return cnt
        
    def checkLeft(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt +=1
                else:
                    return cnt
        except:
            return cnt
        
    def checkUpLeft(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt +=1
                else:
                    return cnt
        except:
            return cnt
        
    def checkUpRight(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt +=1
                else:
                    return cnt
        except:
            return cnt
        
    def checkDownRight(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt +=1
                else:
                    return cnt
        except:
            return cnt
        
    def checkDownLeft(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt +=1
                else:
                    return cnt
        except:
            return cnt
        
    def btnClick(self): 
        # for i in range(len(self.pb2D)):
        #     for j in range(len(self.pb2D[i])):
        #         if self.pb2D[i][j] == self.sender():
        #             if self.turn%2==0 and self.arr2D[i][j] ==0:
        #                 self.arr2D[i][j] = 1
        #                 self.turn += 1
        #             elif self.turn%2==1 and self.arr2D[i][j] ==0:
        #                 self.arr2D[i][j] = 2
        #                 self.turn += 1
        #
        # self.myrender()
        #------------------------------------------------------------------
        # x,y = map(int,self.sender().toolTip().split(","))  
        # if self.arr2D[x][y] == 0 and self.turn%2 == 0 :
        #     self.arr2D[x][y] = 1
        #     
        # elif self.arr2D[x][y] == 0 and self.turn%2 == 1:
        #     self.arr2D[x][y] = 2   
        # self.turn += 1
        # self.back2D.append(str(x)+","+str(y))
        # self.myrender()
        #------------------------------------------------------------------
        if self.flag_over:
            return
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j]>0:
            return
        stone = -1
        if self.turn%2 == 0:
            self.arr2D[i][j]=1
            stone = 1
        else:
            self.arr2D[i][j]=2
            stone = 2
            
        u = self.checkUP(i,j,stone)
        d = self.checkDown(i, j, stone)
        r = self.checkRight(i, j, stone)
        l = self.checkLeft(i, j, stone)
        ur = self.checkUpRight(i, j, stone)
        ul = self.checkUpLeft(i, j, stone)
        dr = self.checkDownRight(i, j, stone)
        dl = self.checkDownLeft(i, j, stone)
        
        d1 = u + d + 1
        d2 = r + l + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1
        color = ""
        if self.turn % 2 == 0:
            color = "흑돌"
        else:
            color = "백돌"
        self.myrender()    
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            QMessageBox.about(self,'승리',color+"승리")
            self.flag_over = True
        
        
        
        self.turn += 1
        self.back2D.append(str(i)+","+str(j))
        
        
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QIcon("0.png"))
                    
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QIcon("1.png"))
                    
                if self.arr2D[i][j] ==2:
                    self.pb2D[i][j].setIcon(QIcon("2.png"))

    
    def back(self):
        bb = self.back2D
        if len(bb) == 0:
            return
        
        x = int(bb[len(bb)-1].split(",")[0])
        y = int(bb[len(bb)-1].split(",")[1])
        
        if self.arr2D[x][y] == 1:
            self.arr2D[x][y] = 0
            self.turn = 0
        else:
            self.arr2D[x][y] = 0
            self.turn = 1
        #bb.pop(-1)
        
        bb.pop(len(bb)-1)
        self.flag_over = False
        self.myrender()
        
        
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()