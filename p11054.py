n=int(input())
a=list(map(int,input().split()))

dp=[0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i]>a[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1

dp2=[0 for i in range(n)]
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if a[i]>a[j] and dp2[i]<dp2[j]:
            dp2[i]=dp2[j]
    dp2[i]+=1

dp3=[dp[i]+dp2[i]-1 for i in range(n)]
print(max(dp3))