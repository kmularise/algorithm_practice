#재귀함수-DP, top down 방식 이용
n=int(input())
d=[0]*(n+1)
def fibo(k):
    if k==1 or k==2:
        return 1
    if d[k]!=0:
        return d[k]
    d[k]=fibo(k-1)+fibo(k-2)
    return d[k]

print(fibo(n),n-2)