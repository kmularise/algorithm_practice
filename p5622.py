s=str(input())
a='ABC DEF GHI JKL MNO PQRS TUV WXYZ'
b=a.split()
k=0
for i in s:
    for j in range(len(b)):
        if i in b[j]:
            m=k+j+3
            k=m
print(k)