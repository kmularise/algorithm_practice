s=str(input())
if s[0]==' 'and s[-1]==' ':
    print(s.count(' ')-1)
elif s[0]!=' ' and s[-1]!=' ':
    print(s.count(' ')+1)
else:
    print(s.count(' '))