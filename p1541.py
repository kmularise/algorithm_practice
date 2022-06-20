a=input().split('-')
minv=0#최솟값
for i in range(len(a)):
    b=map(int,a[i].split('+'))
    if i==0:
        minv+=sum(b)
    else:
        minv=minv-sum(b)

print(minv)