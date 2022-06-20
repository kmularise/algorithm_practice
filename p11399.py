#26분 정도
n=int(input())
a=list(map(int,input().split()))

a.sort()
s=0#합을 나타냄
for i in range(n):
    for j in range(i+1):
        s+=a[j]
print(s)
'''
b=[0 for i in range(n)]
for i in range(n):
    if i==0:
        b[i]=a[i]
    else:
        b[i]=b[i-1]+a[i]
print(sum(b))
'''