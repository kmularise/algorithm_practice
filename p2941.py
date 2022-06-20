s=str(input())
l={'c=','c-','d-','lj','nj','s=','z='}
n=0
k=0
while n<len(s):
    if s[n:n+3]=='dz=':
        k+=1
        n=n+3
    elif s[n:n+2] in l:
        k+=1
        n=n+2
    else:
        k+=1
        n=n+1
print(k)