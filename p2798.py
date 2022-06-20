n, m=map(int, input().split())
a=list(map(int, input().split()))
t=0
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            if i!=j and j!=k and k!=i:
                if m>=a[i]+a[j]+a[k]>t:
                    t=a[i]+a[j]+a[k]

print(t)
