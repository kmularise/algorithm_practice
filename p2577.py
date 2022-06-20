a=int(input())
b=int(input())
c=int(input())
k=a*b*c
d=[]
n=0
while n<=20:
    a=k//10
    d.append(k%10)
    n=+1
    if k<10:
        break

    k=a
for i in range(10):
    print(d.count(i))
# k=a 순서에 따라 출력값이 달라짐. 주의할 필요 있다.
