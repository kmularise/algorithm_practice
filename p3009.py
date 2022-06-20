
x=[]
y=[]
for i in range(3):
    a, b=map(int,input().split())
    x.append(a)
    y.append(b)
x1=0
y1=0

if x[0]==x[1]:
    x1=x[2]
elif x[1]==x[2]:
    x1=x[0]
elif x[0]==x[2]:
    x1=x[1]

if y[0]==y[1]:
    y1=y[2]
elif y[1]==y[2]:
    y1=y[0]
elif y[0]==y[2]:
    y1=y[1]
print(x1,y1)