n=int(input())
a=[]
for _ in range(n):
    b=int(input())
    a.append(b)
a.sort()
id=0 #등장 횟수 count
max1=0# 최빈값 횟수
c=-4001
ct=0# 두번째로 작은 거 찾기 위한 거 ct=1이면 멈춤
if n==1:
    c=a[0]
else:
    for i in range(n):
        id+=1
        if (i<n-1 and a[i+1]!=a[i]) or i==n-1:#i=n-1 if문 무조건 시행
            if id>max1:
                max1=id
                c=a[i]
                ct=0
            if id==max1:
                ct+=1
                if ct==2:
                    c=a[i]
            id=0

print(int(round((sum(a)/n),0)))
print(a[(n-1)//2])
print(c)
print(a[-1]-a[0])
