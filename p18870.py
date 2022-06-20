import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
b=[]
'''for i in enumerate(a):
    b.append(i)18870 블로그 문제든 뭐든 참조'''
for i in range(n):
    b.append((a[i],i))
b.sort()

c=[0 for i in range(n)]
ct=0#세는 횟수
for i in range(n):
    if i>0 and b[i-1][0]!=b[i][0]:
        ct+=1
    c[int(b[i][1])]=ct

for i in range(n):
    if i==n-1:
        print(c[i],end='')
    else:
        print(c[i],end=' ')
'''import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
a.sort()


for i in a:
    print(b.index(i), end=' ')

for i in range(n):
    ct=0#좌표 압축 counting
    for j in set(a):
        if j<a[i]:
            ct+=1
    if i==n-1:
        print(ct,end='')
    else:
        print(ct,end=' ')'''