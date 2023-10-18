# 가위/바위/보를 선택하세요
# 나 : 가위
# 컴 : 보
# 결과 : 이김
from random import random

mine = input("가위/바위/보를 선택하세요 ")
arr = ["가위","바위","보"]
rnd = int(random()*3)
com = arr[rnd]
res =""

if mine == com:
    res = "비김"
elif (mine,com) in [("가위","바위"),("바위","보"),("보","가위")]:
    res = "패배"
elif (mine,com) in [("가위","보"),("바위","가위"),("보","바위")]:
    res = "승리"
else:
    res = "잘못된 입력값"
    
print("나 :",mine)
print("컴 :",com)
print("결과 :",res)