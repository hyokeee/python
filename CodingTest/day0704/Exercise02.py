
arr = []
txt = ""
for i in range(5):
    a = input()
    arr.append(a)
    
max_len = 0
for i in range(5):
    if len(arr[i])>=max_len:
        max_len = len(arr[i])
        
for i in range(5):
    for j in range(len(arr[i]),max_len):
        arr[i] = arr[i]+" "
         
for i in range(5):
    for j in range(max_len):
        txt += str(arr[j][i])

print(txt.replace(" ", "",))