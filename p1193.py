from fractions import Fraction
n=int(input())
l=0
k=0
while n>k:
    l+=1
    k+=l
t=n-(k-l)

if l%2==1:
    print('%d/%d'%((l+1-t),t))
else:
    print('%d/%d'%(t,(l+1-t)))

#print(Fraction(t,(l+1-t)))

#print('%d/%d'%(t,(l+1-t)))