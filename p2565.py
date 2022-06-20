#LIS이용
n=int(input())
x=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append([a,b])

x.sort()

dp=[0]*n

for i in range(n):
    for j in range(i):
        if x[i][1]>x[j][1] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(n-max(dp))