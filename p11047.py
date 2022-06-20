#8분
n,k=map(int,input().split())
a=k
ct=0
b=[]
for i in range(n):
    x=int(input())
    b.append(x)

for i in range(n-1,-1,-1):
    if a//b[i]!=0:
        ct+=a//b[i]
        a=a%b[i]

print(ct)
