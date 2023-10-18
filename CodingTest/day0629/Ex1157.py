a = input().lower()

alist = list(set(a))

cnt_list = []
for i in alist:
    cnt = a.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) >1:
    print("?")
else:
    index = cnt_list.index(max(cnt_list))
    print(alist[index].upper())