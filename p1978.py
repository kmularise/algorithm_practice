n=int(input())#주어진 수 n개
data=list(map(int, input().split()))
pn=0#소수의 개수 나타내는 파라미터
for i in data:
    m=1#1이면 i는 소수 0이면 소수 아님
    j=2#2부터 나누기 시작
    if i==1:
        m=0
    while j<=i*0.5:
        if i%j==0:
            m=0
            break
        j+=1#while에서 더해주는거 꼭 체크!
    pn+=m

print(pn)