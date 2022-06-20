n=int(input())
if n==1:
    n=0
else:
    m=n#소인수 분해에 쓰일 파라미터
    for i in range(2,n+1):#조건 주의 이대로만 써도 된다.
        if n%i==0:
            a=i#소수라면 i 그대로 받고, 아니면 0
            for j in range(2,int((i**0.5)//1)+1):
                if i%j==0:
                    a=0#i는 소수가 아니다.
                    break
            if a==i:
                for _ in range(2,100):
                    if m%a!=0:
                        break
                    print(a)
                    mm=m//a
                    m=mm

