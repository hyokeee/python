from random import random


#Strike 구하는 메서드
def getS(com,mine):
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


#Ball 구하는 메서드
def getB(com,mine):
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


# 컴퓨터 값 셋팅 메서드
def ranC():
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


com = ranC()
#while 변수
w = True
while w:
    
    # 내 입력값 받기
    mine = input("숫자를 맞춰보세요 : ")
    print(com)
    # 내 입력값으로 Strike, Ball 값 받기
    s = getS(com,mine)
    b = getB(com,mine)
    
    
    # 결과 출력
    if s == 3:
        print(mine,"\t","정답입니다")
        w = False
    else:
        print(mine,"\t",str(s)+"S"+str(b)+"B")