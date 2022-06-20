m=int(input())
n=int(input())
k=0
pn=0 #pn은 소수 개수 카운터
sum=0 #sum은 소수 합 나타냄
fn=0#fn은 첫번째로 나오는소수
for i in range(m,n+1):
    j=2#j는 소수 2부터 시작
    t=1#t=1이면 소수, t=0이면 소수 아님
    if i==1:
        t=0#1은 소수가 아니다.
    while j<=(i**0.5):
        if i%j==0:
            t=0
            break
        j+=1
    pn+=t#pn=1일 때 제일 작은소수
    if pn==1 and t==1:#소수이면서 첫번째
        fn=i
    if t==1:
        sum+=i
if pn!=0:
    print(sum)
    print(fn)
else:
    print(-1)