k=int(input())
x=[]
b=[]
for i in range(6):
    a, y=map(int,input().split())
    x.append(a)
    b.append(y)

x1=max(b[0],b[4],b[2])#가로나 세로의 최댓값 중 하나
x2=max(b[1],b[3],b[5])

y1=b[2]
y2=b[3]
for i in range(5):
    if b[i]*b[i+1]==x1*x2:#각각이 최댓값이면 곱도 최댓값
        y1=b[(i+3)%6]#빼야하는 사각형은 첫번째 최대값 인덱스 +3,+4길이의 곱
        y2=b[(i+4)%6]
c=x1*x2-y1*y2
print(k*c)