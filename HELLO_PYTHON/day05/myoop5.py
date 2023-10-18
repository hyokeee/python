class LeeJY:
    def __init__(self):
        self.cnt_company = 10
        
    def hit(self,punch):
        self.cnt_company += punch
        
    def __del__(self):
        pass
    
    def __str__(self):
        return str(self.cnt_company)
    
class Biden:
    def __init__(self):
        self.head_color = "white"
        
    def dye(self):
        self.head_color = "red"
        
    def __del__(self):
        pass
    
    def __str__(self):
        return self.head_color
    
class Musk:
    def __init__(self):
        self.cnt_sat = 1000
        
    def launch(self):
        self.cnt_sat += 10
        
    def __del__(self):
        pass
    
    def __str__(self):
        return str(self.cnt_sat)
    

class Eunbi(LeeJY,Biden,Musk):
    def __init__(self):
        LeeJY.__init__(self);
        Biden.__init__(self);
        Musk.__init__(self);
        print("나는 은비,LeeJY,Biden,Musk를 상속!")
    
    
    def __del__(self):
        pass
    
    def __str__(self):
        return "은비 아빠 회사 갯수 "+str(self.cnt_company)+" 은비 아빠 머리색 "+str(self.head_color)+" 은비 아빠 위성 갯수 "+str(self.cnt_sat)
    
    
    
    
if __name__ == '__main__':
        
    # l = LeeJY()
    # b = Biden()
    # m = Musk()
    #
    # print(l)
    # print(b)
    # print(m)
    
    e = Eunbi()
    
    print(e)
    e.hit(3)
    e.dye()
    e.launch()
    
    print(e)