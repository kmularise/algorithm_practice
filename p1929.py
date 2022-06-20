m, n=map(int,input().split())
for i in range(m,n+1):
    if i==1:
        continue
    else:
        pind=0#소수이면 0, 아니면 1
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                pind=1
                break
        if pind==0:
            print(i)