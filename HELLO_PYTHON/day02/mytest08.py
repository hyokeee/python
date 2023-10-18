# 출력할 구구단을 입력하세요 7
# 7*1 = 7
# 7*9 = 63

gugu = int(input("출력할 구구단을 입력하세요 "))


for i in range(1,9+1):
    res = gugu * i
    print("{} * {} = {}".format(gugu,i,res))