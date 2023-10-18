# 1~45까지 수 중에서 로또 만드세요
from random import random

arr = []


for i in range(1,45+1):
    arr.append(i)
    

for i in range(100):
    rnd = int(random()*45)
    temp = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = temp


print("로또번호는 {} 입니다.".format(sorted(arr[:6])))

