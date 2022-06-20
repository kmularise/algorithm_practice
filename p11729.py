def htn(n,s,v,to1):
    k=0
    if n==1:
        return 1
    else:
        return htn(n-1,s,v,to1)+1+htn(n-1,v,to1,s)#사실 htn(n-1,s,v,to1)=htn(n-1,v,to1,s)임을 알 수 있음
def htop(n,start,to,via):
    if n==1:
        print(start,to)
        return
    else:
        htop(n-1,start,via,to)
        print(start,to)
        htop(n-1,via,to,start)
    return
k=int(input())
print(htn(k,1,3,2))
htop(k,1,3,2)