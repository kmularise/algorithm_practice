n=int(input())
a=[[] for i in range(201)]
for i in range(n):
    x, y=input().split(" ")    
    a[int(x)].append((int(x),str(y)))

for i in a:
    if i!=[]:
        for j in i:
            print(j[0],j[1])
