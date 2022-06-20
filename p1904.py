import sys
input=sys.stdin.readline
n=int(input())
d=[0]*(n+1)
def fire(k):
    #피보나치 나머지
    if k==0 or k==1:
        return 1
    if d[k]!=0:
        return d[k]
    d[k]=(fire(k-1)+fire(k-2))%15746
    return d[k]
print(fire(n))
#재귀함수 쓰면 runtime error난다.