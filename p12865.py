#냅색 알고리즘..장렬히 전사
n, k=map(int,input().split())
a=[]
for i in range(n):
    x, y=map(int,input().split())#x 무게, y 가치
    a.append([x,y])

dp=[0 for i in range(n)] # 가치담는 배열
dp1=[0 for i in range(n)] # 무게 담는 배열
for i in range(n):
    if dp1[i]==0 and a[i][0]>k:
        continue
    for j in range(i):
        if dp1[j]+a[i][0]<=k and dp[i]<dp[j]:
            dp[i]=dp[j]
            dp1[i]=dp1[j]
    dp[i]+=a[i][1]
    dp1[i]+=a[i][0]

print(max(dp))
