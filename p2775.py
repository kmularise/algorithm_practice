t=int(input())
for __ in range(t):
    k=int(input())
    n=int(input())
    s=[i+1 for i in range(n)]
    for _ in range(1,k+1):
        for i in range(1,n):
            s[i]+=s[i-1]
    print(s[-1])
