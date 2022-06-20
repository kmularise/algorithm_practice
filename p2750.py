#삽입정렬로 풀겠습니다.
def insertion_sort(M):
    for i in range(1,len(M)):
        for j in range(i,0,-1):
            if M[j-1]>M[j]:
                M[j-1],M[j]=M[j],M[j-1]#이렇게도 할당할 수 있음


n=int(input())#정수의 개수
a=[]
for _ in range(n):
    x=int(input())
    a.append(x)
insertion_sort(a)

for k in a:
    print(k)