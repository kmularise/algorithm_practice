w,h,x,y,p=map(int,input().split())
ct=0#선수의 수
r=h//2
for i in range(p):
    x1,y1=map(int,input().split())
    c1=(x1-x)**2+(y1-r-y)**2
    c2=(x1-x-w)**2+(y1-r-y)**2
    if x1 in range(x,x+w+1) and y1 in range(y,y+h+1):
        ct+=1
    elif c1<=r**2 or c2<=r**2:#경계선 포함이라는 건 문제에서 안알려주나..
        ct+=1

print(ct)
