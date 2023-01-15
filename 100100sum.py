import sys
sys.stdin = open("input.txt","r")
import copy

for t in range(10):
    test_num = int(input())
    sumtab = []
    temp = 0
    table=[[0]*100]*100
    for i in range(100):
        table[i] = list(map(int,input().split()))
        for j in range(100):
            temp = temp + table[i][j]
        sumtab.append(temp)
        temp = 0   
    for i in range(100):
        for j in range(100):
            temp = temp + table[j][i]
        sumtab.append(temp)
        temp = 0   
    for i in range(100):
        temp = temp + table[i][i]
    sumtab.append(temp)
    temp = 0        
    for i in range(100):
        temp = temp + table[99-i][i]    
    sumtab.append(temp)        
    sumtab.sort()
    print(f'#{test_num} {sumtab.pop()}')