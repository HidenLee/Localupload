import copy
countnum = 0
def scale(numlist,ltotal,rtotal):
    global countnum
    if rtotal > ltotal:
        print(numlist,ltotal,rtotal,"fail",countnum)
        return
    if numlist == []:
        countnum += 1
        print(numlist,ltotal,rtotal,"end",countnum)  
        return 1 
    for i in range(len(numlist)):   
        localt = numlist[i]
        newlist = copy.deepcopy(numlist)
        print("keep",newlist,ltotal,rtotal)   
        newlist.remove(localt)
        scale(newlist,ltotal+localt,rtotal)
        scale(newlist,ltotal,rtotal+localt)
        newlist.append(localt)   
    return countnum       
T = int(input())
for test_case in range(T):
    linnum= int(input())
    target = list(map(int,input().split()))
    scale(target,0,0)
    print(f'#{test_case+1} {countnum}')
    countnum = 0 