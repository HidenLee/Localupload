def scale(linnum,numlist):
    visited = [False] * linnum
    pow = [1,2,4,8,16,32,64,128,256,512]
    fac = [1,1,2,6,24,120,720,5040,40320,362880]
    countnum = 0
    def calculatescale(total,ltotal,rtotal,idx):
        nonlocal countnum
        global linnum
        if (ltotal*2 > total):
            countnum += (pow[linnum-idx] * fac[linnum-idx])
            return
        if idx == linnum:
            countnum += 1
            return 
        for i in range(len(numlist)):
            if not visited[i]:
                visited[i] = True  
                localt = numlist[i]
                calculatescale(total,ltotal+localt,rtotal,idx+1)
                if ltotal >= rtotal+localt:
                    calculatescale(total,ltotal,rtotal+localt,idx+1)
                visited[i] = False
    calculatescale(sum(numlist),0,0,0)
    return countnum

T = int(input())
for test_case in range(T):
    linnum= int(input())
    target = list(map(int,input().split()))
    print(f'#{test_case+1} {scale(linnum,target)}')

