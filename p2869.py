a, b, c=map(int, input().split())
if (c-a)%(a-b)==0:
    print((c-a)//(a-b)+1)
else:
    print((c-a)//(a-b)+2)