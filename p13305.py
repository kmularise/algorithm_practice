#import sys
#print(sys.getrecursionlimit()) - 값이 1000이 나옴
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
min=b[0] #a[i]까지의 최솟값 recursion error?-import sys 쓰면 발생
cost=0 #최소비용
for i in range(n-1):
    if b[i]<min:
        min=b[i]
    cost+=min*a[i]

print(cost)
