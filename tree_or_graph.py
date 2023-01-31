import sys
sys.stdin  = open('input (4).txt','r')

def ancestor(): # int(ancestor), int(size) return
    a = list(map(int,input().split())) 
    totalnode, target1, target2 = a[0],a[2],a[3]
    totallist = list(map(int,input().split()))
    #make node dictionary {parents:sons}
    totaldict = {}
    for roops in range(totalnode-1):
        print(totallist[roops*2],totallist[roops*2+1])
        if totallist[roops*2] in totaldict.keys():
            totaldict[totallist[roops*2]+totalnode] = totallist[roops*2+1] 
        else:
            totaldict[totallist[roops*2]] = totallist[roops*2+1] 

    #for find common ancestor, make each list of parents
    while True:
        temp = 0
        
        break
    print(t1plist)
    # for elm in t1plist:
    #     if elm > totalnode:
    #         elm -= totalnode    
    t2plist=list(filter(lambda elem : elem[1] == target2, totaldict.items()))
    # for elm in t2plist:
    #     if elm > totalnode:
    #         elm -= totalnode
    intersection = list(set(t1plist) & set(t2plist))
    print(intersection)
    return 





t = int(input())
for test_case in range(t):
    print(f'#{test_case+1} {ancestor()}')
