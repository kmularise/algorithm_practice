n=int(input())
k=2000000
mn=0
#mn=[]
for i in range(n):
    l=0
    for j in range(len(str(i))):
        l+=(i//(10**j))%10
    m=i+l
    if m==n and m<k:
        k=m
        mn=i
        #mn.adppend(i)
print(mn)
#min(mn)