t=int(input())

for i in range(t):
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    ct=0#진입, 이탈횟수

    for j in range(n):
        cx,cy,r=map(int,input().split())
        a=0
        a1=(x1-cx)**2+(y1-cy)**2
        a2=(x2-cx)**2+(y2-cy)**2
        if a1<r**2:
            a+=1
        if a2<r**2:
            a+=1
        ct+=(a%2)
    print(ct)
