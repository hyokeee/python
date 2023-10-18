# 첫수를 입력하세요 7
# 끝수를 입력하세요 9
# 7은 9보다 2만큼 작습니다

a = int(input("첫 수를 입력하세요 "))
b = int(input("끝 수를 입력하세요 "))

c = a - b

res = ""

if c>0:
    res = "{}은 {}보다 {}만큼 크다".format(a,b,c)
elif c<0:
    res = "{}은 {}보다 {}만큼 작다".format(a,b,abs(c))
else:
    res = "같은 숫자입니다"
    
print(res)

