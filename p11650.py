n=int(input())
a=[]#튜플저장소
for i in range(n):
    x, y=map(int,input().split())
    a.append((x,y))

a.sort()
for i in a:
    print(i[0], i[1])