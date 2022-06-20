n=int(input())
arr=[]
comp=[1 for _ in range(n)]#순위비교의 지표
for _ in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])
for i in range(n):
    for j in range(i):
        if arr[i][0]>arr[j][0] and arr[i][1]>arr[j][1]:
            comp[j]+=1
        if arr[j][0]>arr[i][0] and arr[j][1]>arr[i][1]:
            comp[i]+=1

for i in range(len(comp)):
    if i==len(comp)-1:
        print(comp[i],end='')
    else:
        print(comp[i],end=' ')