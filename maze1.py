''' 
(0,0) ~ (15,15) 256칸의 미로
시작점은 (1,1), 도착점은(13,13)로 고정
지역값 0은 길, 1은 벽, 2는 시작점, 3은 도착점
해결 가능한 미로라면 1을 반환, 불가능하면 0을 반환
'''
# 미로의 성공여부를 판단하는 함수, 미로는 2-D array로 인풋예정
# 10개의 테스트케이스/// 각 테스트케이스의 넘버\n미로가 인풋



def maze1(target):
    
    return 0



# 전체 테스트케이스를 입력~ 함수돌리고 각각 출력~
import copy
import sys
sys.stdin = open("input (2).txt", "r")
wholeinput = [[[False*16]]*16]*10
for testcase in range (10):
    maze = [False*16]*16
    t = int(input())
    for roops in range (16):
        wholeinput[testcase][roops] = list(map(int,input().split()))
    maze[testcase] = copy.deepcopy(wholeinput[testcase])
    print(f'#{testcase+1} {maze1(maze[testcase])}')



