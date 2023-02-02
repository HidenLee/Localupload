import sys
sys.stdin = open('input (5).txt','r')

inf = float('inf')

T = int(input())
for test_case in range(T):
    N = int(input()) # size of map
    y = x = 0
    diggingmap = [[inf]*N for _ in range(N)]
    visitlist = [[False]*N for _ in range(N)]
    realmap = [[0]*N]
    for roop in range(N):
        realmap[roop] = list(map(int,input().split()))

    while True:
        pass



