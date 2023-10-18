# 홀 / 짝을 선택하세요 홀
# 나 : 홀
# 컴 : 홀
# 결과 : 승리 / 패배
from random import random

me = input("홀 / 짝을 선택하세요 ")

# arr = ["홀","짝"]
# rnd = int(random()*2)
# com = arr[rnd]

rnd2 = random()
com2 = ""
result = ""
if rnd2 > 0.5:
    com2 = "홀"
else:
    com2 = "짝"

if me == com2:
    result = "승리"
else:
    result = "패배"
    
    
print("나 : {}".format(me))
# print("컴 : {}".format(com))
print("컴2 :{}".format(com2))
print("결과 : {}".format(result))