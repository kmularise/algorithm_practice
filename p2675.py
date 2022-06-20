n=int(input())
for i in range(n):
    a, b=input().split()
    a=int(a)
    b=str(b)
    k=''
    p=''

    for j in range(len(b)):
        p=k+b[j]*(a)
        k=p
    print(p)