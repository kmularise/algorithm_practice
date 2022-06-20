n=int(input())
l=1
i=1
while n>l:
    l+=6*i
    i+=1

print(i)
'''
for i in range(n):
    if n>l:
        l+=6*(i+1)
    elif n==1:
        print(1)
    if n<=l:
        print(i+2)
        break
'''