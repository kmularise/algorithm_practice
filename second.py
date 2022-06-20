n=int(input())
dp=[[[] for j in range(i+1)] for i in range(n)]
a=0
for i in range(n):
    for j in range(i+1):
        dp[i][j]+=dp[i-1][j]
        dp[i][j].append(i)

print(dp)
