#어렵다..n=1,2,3일때도 따로 고려해줘야 함
import sys
input=sys.stdin.readline

n=int(input())
b=[]
for i in range(n):
    x=int(input())
    b.append(x)
d=[0]*(n+3)
d[0]=b[0]
if n==1:
    print(d[n-1])
else:
    d[1]=max(b[0]+b[1],b[1])
    if n==2:
        print(d[n-1])
    else:
        d[2]=max(b[0]+b[2],b[1]+b[2])
        if n==3:
            print(d[n-1])
        else:
            for i in range(3,n):
                d[i]=max(d[i-2]+b[i],d[i-3]+b[i]+b[i-1])#이전경로가 최댓값인지, i항과 조건이동일하여 반복되는지
            print(d[n-1])
