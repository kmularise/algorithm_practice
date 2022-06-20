def star(n):
    if n==1:
        return ['*']
    
    a=star(n//3)
    L=[]

    for i in a:
        L.append(i*3)
    for i in a:
        L.append(i+' '*(n//3)+i)
    for i in a:
        L.append(i*3)
    return L
N=int(input())
print('\n'.join(star(N)))