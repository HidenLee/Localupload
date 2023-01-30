'''
고객의 수 N은 2≤N≤10 이다.

그리고 회사의 좌표, 집의 좌표를 포함한 모든 N+2개의 좌표는 서로 다른 위치에 있으며 좌표의 값은 0이상 100 이하의 정수로 이루어진다.
가장 첫줄은 전체 테스트케이스의 수이다.

이후, 두 줄에 테스트 케이스 하나씩이 차례로 주어진다.

각 테스트 케이스의 첫째 줄에는 고객의 수 N이 주어진다. 둘째 줄에는 회사의 좌표,집의 좌표, N명의 고객의 좌표가 차례로 나열된다.

좌표는 (x,y)쌍으로 구성되는데 입력에서는 x와 y가 공백으로 구분되어 제공된다.

총 10줄에 10개의 테스트 케이스 각각에 대한 답을 출력한다.

각 줄은 ‘#x’로 시작하고 공백을 하나 둔 다음 최단 경로의 이동거리를 기록한다. 여기서 x는 테스트 케이스의 번호다.


회사에서 출발해서 이들을 모두 방문하고 집에 돌아가는 경로 중 총 이동거리가 가장 짧은 경로를 찾는 프로그램을 작성하라.
'''
import sys
sys.stdin = open("input (3).txt", "r")
from itertools import permutations
def zipuro(list1):
    
    
    def distance(tup1,tup2): # 두 점간의 거리를 구하는 함수
        return abs(tup1[0]-tup2[0])+ abs(tup1[1]-tup2[1])
    

    #distances[n][m] = n좌표와 m좌표 사이의 거리
    distances =[[0]*len(list1) for _ in range(len(list1))] #배열 초기화, len*len의 형식을 취하지 않은 이유는 모두 같은 객체로 인식되는걸 막기 위함, _는 단순 반복을 의미
    for broop in range(len(list1)): # list = [1,2,3,4,5] ,len(list) = 5 => 0,1,2,3,4
        for sroop in range(1,len(list1)-broop): # 1,2,3,4 / 1,2,3 / 1,2 / 1 / none
            distances[broop][broop+sroop] = distance(list1[broop],list1[broop+sroop]) # 0,1~0,4 / 1,2~1,4 / 2,3~2,4 / 3,4 / none

    #배열을 섞기 1번 2번튜플 제외 나머지의 배열을 섞기
    def shuffle(list2):
        start = list2.pop(0)
        end = list2.pop(0)
        alllist = []
        temp = list(permutations(list2,len(list2)))
        for perm in temp:
            newlist = []
            newlist.append(start)
            for elem in perm:
                newlist.append(elem)    
            newlist.append(end)
            alllist.append(newlist)
        return alllist
    
    shufflelist = shuffle(list(range(len(list1)))) # 0~N-1으로 대체해서 섞음
    sumlist = []
    for lists in shufflelist:
        temp = 0
        for roop in range(len(lists)-1):
            if distances[lists[roop]][lists[roop+1]] != 0:
                temp += distances[lists[roop]][lists[roop+1]]
            else:
                temp += distances[lists[roop+1]][lists[roop]]    
        sumlist.append(temp)
    sumlist.sort()
    print(sumlist)
    return sumlist[0]

T = int(input())
for test_case in range(1, T + 1):
    a = int(input())
    list1 = list(map(int,input().split()))
    list2 = []
    for roop in range(a):
        list2.append((list1[2*roop] , list1[2*roop+1]))    
    print(f'#{test_case} {zipuro(list2)}')	
