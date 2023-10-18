# 1~9까지 무작위로 세자리 수 (중복 없이) 만들기
# 맞출 때까지 무한반복
# 숫자를 맞춰보세요 : "입력"
# 같은 자리의 수가 있으면 strike, 같은 수가 다른 자리에 있으면 ball
# com = "329" , mine ="123" ==> 123 1S1B
# com = "329" , mine = "321" ==> 321 2S0B
# com = "329", mine ="329" ==> 329 맞췄습니다. 프로그램 종료
from random import random
#while
con = True

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
print(com)

while con:
    strike = 0
    ball = 0
    
    mine = input("숫자를 맞춰보세요 : ")
    if com == mine:
        print(mine,"\t","맞췄습니다.")
        con = False
    else:
        if com[0] == mine[0]:
            strike += 1
        if com[1] == mine[1]:
            strike += 1
        if com[2] == mine[2]:
            strike += 1
            
        if com[0] == mine[1] or com[0] == mine[2]:
            ball +=1
        if com[1] == mine[0] or com[1] == mine[2]:
            ball +=1
        if com[2] == mine[0] or com[2] == mine[1]:
            ball +=1
    
        print(mine,"\t",str(strike)+"S"+str(ball)+"B")
    
    
    