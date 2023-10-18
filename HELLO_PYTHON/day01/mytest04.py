# 첫 수를 입력하시오 1
# 끝 수를 입력하시오 10
# 배수를 입력하시오 5
# 1에서 10까지 5의 배수의 합은 15입니다.

a = input("첫 수를 입력하시오 ")
b = input("끝 수를 입력하시오 ")
c = input("배수를 입력하시오 ")


arr = range(int(a),int(int(b)/int(c))+1)

mySum = 0;
for i in arr:
    mySum = mySum + i*int(c)

print("{}에서 {}까지 {}의 배수의 합은 {}입니다.".format(a,b,c,mySum))