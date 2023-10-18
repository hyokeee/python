class Animal:
    def __init__(self):
        print("난 animal생성자!")
        self.flag_sound = True
        
    def bbeonuri(self):
        self.flag_sound = False

    def __del__(self):
        print("난 animal소멸자!")
        
        
    def __str__(self):
        return "소리능력 "+str(self.flag_sound)
    
class Human(Animal):
    def __init__(self):
        super().__init__()
        print("난 human생성자!")
        self.community_skill = 0

    def momstouch(self,punch):
        self.community_skill += punch
    
    def __del__(self):
        print("난 human소멸자!")
    
    def __str__(self):
        return "커뮤니티스킬 " + str(self.flag_sound) +" " + str(self.community_skill)
        
if __name__ == '__main__':
    
    # a = Animal()
    #
    # print("oop1",a)
    # a.bbeonuri()
    # print("oop1",a)
    
    
    b = Human()
    print(b.flag_sound)
    print(b.community_skill)
    print(b)
    b.momstouch(5)
    b.bbeonuri()
    print(b.flag_sound)
    print(b.community_skill)
    print(b)


        