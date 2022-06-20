n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a.append(x)
dp=[0]*(n+3)
if n>=1:
    dp[0]=a[0]
if n>=2:
    dp[1]=dp[0]+a[1]
if n>=3:
    dp[2]=max(a[0]+a[1],a[2]+a[0],a[1]+a[2])
if n>=4:
    for i in range(3,n):
        dp[i]=max(dp[i-1],dp[i-2]+a[i], dp[i-3]+a[i-1]+a[i])

print(dp[n-1])
