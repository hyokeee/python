class Vehicle:
    def __init__(self):
        self.wheel_cnt = 2
        
    def flex(self):
        self.wheel_cnt = 4
        
    def __del__(self):
        pass
    
    def __str__(self):
        return "바퀴 갯수 : " + str(self.wheel_cnt)+"개"    
    
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.autopilot_level = 1
        
    def hit(self):
        self.autopilot_level += 1
    
    def __del__(self):
        pass
    
    def __str__(self):
        return "오토파일럿레벨 : " + str(self.autopilot_level)
    
if __name__ == '__main__':
    v = Vehicle()
    print(v)
    v.flex()
    print(v)
    
    c = Car()
    print(c)
    print(c.wheel_cnt)
    
    c.flex()
    c.hit()
    
    print(c)
    print(c.wheel_cnt)
    
    c.hit()
    print(c)
    