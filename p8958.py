n=int(input())
for j in range(n):
    a=str(input())
    l=0
    s=0
    for i in a:
        if i=='X':
            l=0
        elif i=='O':
            l+=1
            s+=l
    print(s)
