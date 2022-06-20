n=int(input())
d=[0]*(n+4)
d[2]=1
d[3]=1
for i in range(4,n+1):
    a=i//2
    b=i%2
    c=i//3
    e=i%3
    if i%2==0:
        a=a/2
        b=b+1
    if i%3==0:
        c=c/3
        e=e+1
    d[i]=min(b+d[int(a*2)],e+d[int(c*3)])

print(d[n])
