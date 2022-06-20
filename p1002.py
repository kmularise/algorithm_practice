n=int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    
    z1=(x1-x2)**2+(y1-y2)**2
    z2=(r1+r2)**2
    z3=(r2-r1)**2
    if x1==x2 and y1==y2 and r1==r2:#제발 어이없는 짓좀 하지말자
        print(-1)
    elif z1==z2 or z1==z3:
        print(1)
    elif z3<z1<z2:
        print(2)
    else:
        print(0)
