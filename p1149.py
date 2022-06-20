n=int(input())
a=[]
for i in range(n):
    r, g, b=map(int,input().split())
    a.append([r,g,b])
#r,g,b 각각 a[i]의 0,1,2에 저장됨

d=[[0,0,0] for i in range(n)]
d[0][0]=a[0][0]
d[0][1]=a[0][1]
d[0][2]=a[0][2]

for i in range(1,n):
    d[i][0]=min(d[i-1][1],d[i-1][2])+a[i][0]
    d[i][1]=min(d[i-1][0],d[i-1][2])+a[i][1]
    d[i][2]=min(d[i-1][1],d[i-1][0])+a[i][2]
print(min(d[n-1]))

