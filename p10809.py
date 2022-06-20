s=str(input())
tt='abcdefghijklmnopqrstuvwxyz'
k=[]
for i in tt:
    if s.count(i)==0:
        k.append(-1)
    else:
        k.append(s.find(i))
for j in k:
    print(j, end=' ')