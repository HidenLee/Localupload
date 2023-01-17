import copy
countnum = 0
pow_l = [0]*10
fac_l = [0]*10
pow_l[0], fac_l[0] = 1, 1
for i in range(1, 10):
    pow_l[i] = pow_l[i-1] * 2
    fac_l[i] = fac_l[i-1] * i
def scale(numlist,ltotal,rtotal,idx):
    global countnum, linnum
    if (ltotal > sum(target) //2):
        countnum += (pow_l[linnum-idx] * fac_l[linnum-idx])
        return
    if numlist == []:
        countnum += 1
        return 
    for i in range(len(numlist)):   
        localt = numlist[i]
        newlist = copy.deepcopy(numlist)
        newlist.remove(localt)
        scale(newlist,ltotal+localt,rtotal,idx+1)
        if ltotal-rtotal-localt >= 0:
            scale(newlist,ltotal,rtotal+localt,idx+1)
        newlist.append(localt)
    return countnum       
T = int(input())
for test_case in range(T):
    linnum= int(input())
    target = list(map(int,input().split()))
    scale(target,0,0,0)
    print(f'#{test_case+1} {countnum}')
    countnum = 0 