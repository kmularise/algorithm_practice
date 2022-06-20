#렬정적인 나 이번엔 선택정렬 꺄륵
n=int(input())
a=[]
for _ in range(n):
    b=int(input())
    a.append(b)

for i in range(n):
    min=10000 #최솟값을 저장
    temp=a[i] #a[i]를 저장해주자.
    ind=0 #최솟값이 있는 위치 저장
    for j in range(i,n):
        if a[j]<min:
            min=a[j]
            ind=j
    a[i]=min
    a[ind]=temp
    
for k in a:
    print(k)