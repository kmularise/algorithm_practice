n=int(input())
k=0
for i in range(n):
    s=str(input())
    sen=''
    kk=0
    if len(s)!=len(set(s)):
        for j in s:
            if s.count(j)>1:
                sen+=j#python은 문자열이어도 된다. 빼기는 안됨

        for i in set(sen):
            if s[s.find(i):s.find(i)+s.count(i)]==i*s.count(i):
                kk+=0
            else:
                kk+=1
        
        if kk==0:
            k+=1


    else:
        k+=1
print(k)