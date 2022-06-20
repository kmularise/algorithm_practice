import sys
#
def func(y, x, str1,d):
    a=0#칠하는 횟수
    for s in range(y,y+8):
        for t in range(x,x+8):
            if (s+t)%2==0 and d[s][t]==str1:
                a+=1
            elif (s+t)%2!=0 and d[s][t]!=str1:
                a+=1
    return a

m,n=map(int,sys.stdin.readline().split())
data=[sys.stdin.readline().strip() for i in range(m)]

'''for j in data:#pythonic한 방법
    for k in j:'''
min1=m*n #최소 칠하는 횟수 64가 더나음 ㅋㅋ
for j in range(m):
    for k in range(n):
        if j+7>=m or k+7>=n:
            continue
        else:
            a=func(j,k,'B',data)
            #b=func(j,k,'W',data)
            if a>32:
                a=64-a#이러면 함수 연산 2번 안해도 됨
            ss=a
            if ss<min1:
                min1=ss

print(min1)
