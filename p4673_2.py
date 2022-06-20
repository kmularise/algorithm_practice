def solve():
    a=set()
    for i in range(1,10001):
        k=0
        for j in range(len(str(i))):
            k+=(i//(10**j))%10
        t=i+k
        a.add(t)
    
    for m in range(1,10001):
        if m not in a:
            print(m)

solve()