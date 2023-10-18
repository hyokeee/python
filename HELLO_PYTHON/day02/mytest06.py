# 1에서 9까지 수 중에서 중복없이 섞어서 3개의 수를 출력하세요.
from random import random


arr = [1,2,3,4,5,6,7,8,9]

for a in range(0,len(arr)):
    rnd = int(random()*9)
    if rnd != a:
        temp = arr[rnd]
        arr[rnd] = arr[a]
        arr[a] = temp

print(arr[:3])

#---------------------------

arr2 = [1,2,3,4,5,6,7,8,9]

for i in range(99):
    r = int(random()*9)
    aa = arr2[0]
    arr2[0] = arr2[r]
    arr2[r] = aa
    
print(arr2[:3])




    

    
    









