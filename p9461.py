#Dp-bottom up 방식
d=[0]*5000
d[1]=1
d[2]=1
d[3]=1
t=int(input())
for i in range(t):
    a=int(input())
    if d[a]!=0:
        print(d[a])
    else:
        for j in range(4,a+1):
            if d[j]!=0:
                continue
            d[j]=d[j-2]+d[j-3]
        print(d[a])
