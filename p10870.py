def pivo(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return pivo(n-1)+pivo(n-2)

a=int(input())
print(pivo(a))