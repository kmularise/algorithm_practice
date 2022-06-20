import sys
def star(n):#시간 초과나는 풀이 81이에서 막혔음
    if n==1:
        a=[[1 for _ in range(3)]for __ in range(3)]
        a[1][1]=0
        return(a)
    b=[[1 for _ in range(3**n)]for __ in range(3**n)]
    for nn in range(3**n):
        for nnn in range(3**n):
            if nn//(3**(n-1))==1 and nnn//(3**(n-1))==1:
                b[nn][nnn]=0
            else:
                b[nn][nnn]=star(n-1)[nn%(3**(n-1))][nnn%(3**(n-1))]
    return(b)
number=int(sys.stdin.readline())
for pp in range(8):
    if 3**(8-pp)==number:
        kk=8-pp
        break      
output=star(kk)
for aa in range(number):
    for bb in range(number):
        if output[aa][bb]==1:
            print('*',end='')
        else:
            print(' ',end='')
    if aa==number:
        break
    print('\n',end='')