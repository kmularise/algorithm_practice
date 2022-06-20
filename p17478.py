def no(n, str1, str2, str3,str4, end):
    if n==0:
        print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
    if n == end:
        print('_'*(4*end)+'"재귀함수가 뭔가요?"')
        print('_'*(4*end)+'"재귀함수는 자기 자신을 호출하는 함수라네"')
        for i in range(end+1):
                print('_'*(4*(end-i))+'라고 답변하였지.')
        return
    print(str1)
    print(str2)
    print(str3)
    print(str4)
    return no(n+1, '_'*4+str1,'_'*4+str2,'_'*4+str3,'_'*4+str4, N)
    
N = int(input())
s1= '"재귀함수가 뭔가요?"'
s2='"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어. '
s3='마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지. '
s4='그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
no(0, s1,s2,s3,s4,N)
