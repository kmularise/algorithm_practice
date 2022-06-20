import sys

n=int(sys.stdin.readline())

b=[0]*10000
#b=[0 for _ in range(10000)]#i+1 해당 자연수,시간 초과 뜬다 ㅂㄷㅂㄷ..
for i in range(n):
    b[int(sys.stdin.readline())-1]+=1
    
for j in range(10000):
    if b[j]!=0:
        for k in range(b[j]):
            sys.stdout.write(str(j+1)+"\n")

