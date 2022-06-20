import sys
n=int(input())
d=list(map(float,sys.stdin.readline().split()))
k=max(d)
x=[]
for i in d:
    x.append((i*100)/k)
print(sum(x)/len(x))
# i는 d의 복사한 값

"""
for i, elem in enumerate(d):
    # elem == d[i]
    print(i, elem)

clothes = ['a', 'b', 'c']
for cloth in clothes:
    print(cloth)
    ..."""