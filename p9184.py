d= [[[0]*21 for j in range(21)] for k in range(21)]

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    if d[a][b][c]!=0:
        return d[a][b][c]
    if a<b and b<c:
        d[a][b][c]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)#여기ㅓ도 d에 저장해줘야 함
        return d[a][b][c]
    d[a][b][c]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return d[a][b][c]

while True:
    A,B,C=map(int, input().split())

    if A==-1 and B==-1 and C==-1:
        break
    print('w(%d, %d, %d) = %d'%(A,B,C,w(A,B,C)))
