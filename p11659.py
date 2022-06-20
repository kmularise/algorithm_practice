n,m=map(int,input().split())
a=list(map(int,input().split()))
s=[0]*n
s[0]=a[0]
for i in range(1,n):
    s[i]=s[i-1]+a[i]

for i in range(m):
    x,y=map(int,input().split())
    if x==1:
        print(s[y-1])
    else:
        print(s[y-1]-s[x-2])

