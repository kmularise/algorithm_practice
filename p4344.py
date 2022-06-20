import sys
n=int(input())
for i in range(n):
    data=list(map(int,sys.stdin.readline().split()))
    s=data[1:]
    mean=sum(s)/data[0]
    k=0
    for j in s:
        if j>mean:
            k+=1
    u=float((k*100)/data[0])
    print('%.3f'%u+'%')