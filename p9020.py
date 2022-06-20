import sys
#에라토스테네스 체 이용
def p_n(n):
    #n 이하 소수 구하기
    s=[1]*(n+1)
    s[1]=0
    s[0]=0#1,0은 소수가 아님

    m=int(n**0.5)#범위를 줄여주자.
    for i in range(2,m+1):#2~m
        if s[i]==1:
            for j in range(i*i,n+1,i):# i*i부터 시작해도됨! 왜냐하면 2*i~(i-1)*i는 지워짐
                s[j]=0
    return s

t=int(sys.stdin.readline())
sn = p_n(10001)
for i in range(t):
    d=int(input())
    for j in range(int(d/2)):
        s1=int(d/2)-j #큰홀수부터 탐색해야 차이가 가장 작게 됨
        s2=int(d/2)+j
        if sn[s1]==1 and sn[s2]==1:
            print(s1, s2)
            break
