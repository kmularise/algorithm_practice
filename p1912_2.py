#모르겠다..
n=int(input())
a=list(map(int,input().split()))

d=[0]*n
d[0]=a[0]
for i in range(1,n):
    d[i]=max(a[i],d[i-1]+a[i])

print(max(d))