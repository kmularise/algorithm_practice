n=int(input())
b=set()
for i in range(n):
    w=str(input())
    b.add(w)
c=list(b)
d=[[] for _ in range(51)]#counting 정렬 이용

for i in c:
    d[len(i)].append(i)
for i in range(51):
    d[i].sort()

#print(d)

for i in range(1,51):
    if d[i]!=[]:
        for j in d[i]:
            print(j)