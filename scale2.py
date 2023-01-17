import copy
#결과값변수 선언
countnum = 0    
# 테스트케이스수 입력
T = int(input())    
for test_case in range(T):  
    #추의 개수
    linnum= int(input())    
    #추 각각의 무게
    numlist = list(map(int,input().split()))
    #새 리스트를 만들어서 깊은 복사
    copylist = copy.deepcopy(numlist) 
    #무게 총합 변수 선언 오른쪽 저울의 무게는 (-) 처리 예정
    total = 0 
    #처음 빠지는 원소 바꿔가며 반복
    for l in range(linnum):
        #제외할 원소를 임시값으로 저장
        temp = numlist[l]
        #남아있는 원소 빼가며 반복
        for k in range(linnum-l):
            #오른쪽합계가 더 커진경우는 버리고 반복
            while total =>0:
                #테이블이 비워졌으면 카운트 올리고 상위루프로 회귀
                if copylist == []:
                    countnum += 1
                    print(copylist,ltotal,rtotal,countnum,"end")
                    break
                #남았으면 지정원소 왼쪽으로 옮김
                else:
                    newlist.remove(temp)
                    ltotal += temp




            

def howmanyminuses(target):
    countminuses = 0
    total = 0
    newlist = copy.deepcopy(target)
    for i in range(len(target)):
        buffer = total
        for j in range(2):
            if total >= 0:
                countminuses +=1
                buffer += (newlist[i])*((-1)**j)
             





for isminus in range(2):
    total += temp*((-1)**isminus)
    if total >= 0:
        count

