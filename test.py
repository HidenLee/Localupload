from itertools import permutations
import sys
sys.stdin = open("input (3).txt", "r") 
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    coords = [int(x) for x in input().split()]
    coords = [[coords[2*i], coords[2*i+1]] for i in range(N+2)]
    work, home, customers = coords[0], coords[1], coords[2:]
 
    opt = float('inf')
    get_dist = lambda l1, l2: abs(l1[0]-l2[0]) + abs(l1[1]-l2[1])
    for paths in permutations(customers):
        dist, prev = 0, work
        for loc in paths:
            dist += get_dist(prev, loc)
            prev = loc
            if opt < dist: break
 
        opt = min(opt, dist + get_dist(prev, home))
 
    print(f'#{test_case} {opt}')