#버블버블팝 버블정렬 해보자.
n=int(input())
a=[]
for _ in range(n):
    b=int(input())
    a.append(b)

for i in range(n):
    for j in range(n-1-i):#i=0일 때 가장 큰게 a[n-1],i=1 두번째로 큰게 a[n-2]..
        if a[j+1]<a[j]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

for k in a:
    print(k)