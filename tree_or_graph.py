import sys
sys.stdin  = open('input (4).txt','r')

def ancestor(): # int(ancestor), int(size) return
    #input
    a = list(map(int,input().split())) 
    totalnode, target1, target2 = a[0],a[2],a[3]
    totallist = list(map(int,input().split()))
    
    #make node dictionary {self:parents}
    totaldict = {}
    for roops in range(totalnode-1):
        totaldict[totallist[roops*2+1]] = totallist[roops*2]

    #for find common ancestor, make each list of parents
    temp = target1
    t1plist = []
    while temp != 1:
        t1plist.append(totaldict[temp])
        temp = totaldict[temp]
    temp = target2
    t2plist = []
    while temp != 1:
        t2plist.append(totaldict[temp])
        temp = totaldict[temp]
    intersection = list(set(t1plist) & set(t2plist)) #intersection means common ancestors
    cpr = 1 # compare value, initial is 1, finally means most rescent common ancestor MRCA
    for elm in intersection: #compare index (from t1plist) among common ancestors
        if t1plist.index(elm) < t1plist.index(cpr): 
            cpr = elm
    MRCA = cpr
    
    #count subtree size
    size = 0
    queue = [MRCA]
    parents = MRCA # ancestor node, initial is MRCA
    while True: 
        if not parents in totaldict.values(): # if present node has no any progeny,
            size += 1 # count + 1
            if queue != []:

                parents = queue.pop() #LILO, move upper once
            else: # when the search is over, break this roop, return size of subtree
                break    
        else: # if present node has one or two progeny
            #progey list
            pdict = dict(filter(lambda elm: elm[1] == parents, totaldict.items()))
            parents = list(pdict.keys())[0]  #move lower once
            totaldict[parents] = 0 # blocking communication between up and low  
            queue.append(parents)
    return MRCA , size-1


t = int(input())
for test_case in range(t):
    a, b = ancestor()
    print(f'#{test_case+1} {a} {b}')
