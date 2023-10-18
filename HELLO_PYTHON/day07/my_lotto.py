from random import random
arr45 = []
#arr45 = list(range(1,45+1))
for i in range(1,45+1):
    arr45.append(i)
lotto = "";
for i in range(1,6+1):
    lotto += str(arr45.pop(int(random()*len(arr45))))+" "

print(lotto)



