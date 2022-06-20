n=int(input())
a=[]#튜플저장소
for i in range(n):
    x, y=map(int,input().split())
    a.append((y,x))
a.sort()
#a.sort(reverse=True)#대입이어서 =하나다.여기선 필요없네..
for i in a:
    print(i[1], i[0])