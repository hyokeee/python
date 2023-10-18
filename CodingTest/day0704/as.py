h,w = map(int,input().split())
n = int(input())
arr = []
for i in range(h):
    arr2 = []
    for j in range(w):
        arr2.append(0)
    arr.append(arr2)
    
for k in range(n):
    i,d,x,y = map(int,input().split())
    for j in range(i):
        if d == 1:
            arr[x-1][y-1] = 1
            x += 1
        elif d == 0:
            arr[x-1][y-1] = 1
            y += 1
            
for i in range(h):
    for j in range(w):
        print(arr[i][j],end=" ")
    print("")
