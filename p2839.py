n=int(input())
a=n//5 #for문에서 최댓값부터 출력하도록 해야함

k=0#if문이 안돌아갈시 -1 처리하기 위한 지표
for i in range((n//3)+1):# n을 3으로 나눈 몫으로 범위를 줄임
    if i<=a and (n-(a-i)*5)%3==0:
        sum=a-i+(n-(a-i)*5)//3
        print(sum)
        k=1
        break
if k==0:
    print(-1)