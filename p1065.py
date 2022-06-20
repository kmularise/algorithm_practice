def m(a):
    if len(str(a))<3:
        answer=a
    else:
        nm=0
        for j in range(100,a+1):
            k=1
            for i in range(len(str(j))-2):
                if (int(str(j)[i+2])-int(str(j)[i+1]))!=(int(str(j)[i+1])-int(str(j)[i])):
                    k=0
                    break
            nm+=k
        answer=99+nm
    
    return answer
nn=int(input())
print(m(nn))