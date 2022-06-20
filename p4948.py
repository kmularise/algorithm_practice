import sys
def p_n(n):
    #소수의 개수 구하기
    s=[1]*(n+1)
    s[1]=0
    s[0]=0#1,0은 소수가 아님

    for i in range(2,n+1):#2~m
        if s[i]==1:
            for j in range(2*i,n+1,i):
                s[j]=0
    return sum(s)

while(num:=int(sys.stdin.readline()))!=0:#0이 안되면 계속 입력
    print(p_n(2*num)-p_n(num))