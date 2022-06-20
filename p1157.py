s=str(input())
h=s.upper()
l='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
k=[]
for i in range(len(l)):
    k.append(h.count(l[i]))
q=0
for j in k:
    if j==max(k):
        q+=1

if q>1:
    print('?')
else:
    print(l[k.index(max(k))])