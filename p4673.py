
def solve():
    for i in range(1,10001):
        new=0
        for j in range(1,i):
            l=0
            for k in range(len(str(j))):
                l+=(j//(10**k))%10
            m=j+l
            if m==i:
                new=1
                break
        if new==0:
            print(i)

solve()