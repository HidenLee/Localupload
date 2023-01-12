import sys
sys.stdin = open("input.txt","r")
import copy
def sdoku():
    a = [[0,0,0,0,0,0,0,0,0]]*9
    ans = list(range(1,10))
    b = [0,0,0,0,0,0,0,0,0]
    c = []
    d = []    
    for i in range(9):
        a[i] = list(map(int, input().split()))
        b = copy.deepcopy(a[i])
        b.sort()
        if b != ans:
            return 0
        else:
            b.clear()            
    for i in range(9):
        for j in range(9):
            c.append(a[j][i])
        c.sort()
        if c != ans:
            return 0
        else:
            c.clear()    
    for k in [0,3,6]:
        for l in [0,3,6]: 
            for i in range(3):
                for j in range(3):
                    d.append(a[i+k][j+l])
            d.sort()
            if d != ans:  
                return 0
            else:
                d.clear()
    return 1      
T = int(input())
for o in range(T):
    print(f'#{o+1} {sdoku()}\n')