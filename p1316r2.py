n=int(input())
k = 0

for _ in range(n):
    s=str(input())
    arr=[0 for m in range(26)]
    j=0
    while j < len(s):
        if arr[ord(s[j])-97]==1:
            k+=1
            break
        arr[ord(s[j])-97]=1
        while j<len(s)-1 and s[j]==s[j+1]:# and, or은 첫번째 나오는 거 먼저 읽고 두번째 읽기
            j+=1
        j+=1

print(n-k)