# def solve():
#     n=int(input())
#     l=list(map(int, input().split()))
#     dp=[0 for _ in range(3**n)]
#     que=[(0,0,0,0)]
#     dp[0]=1
#     res=0
#     while que:
#         r=set([])
#         for _ in range(len(que)):
#             ind,k,a,b=que.pop()
#             if k==((1<<n)-1):
#                 res+=dp[ind]
#                 continue
#             for i in range(n):
#                 if k&(1<<i)==0:
#                     if a+l[i]>=b:
#                         dp[ind+(3**i)]+=dp[ind]
#                         r.add((ind+(3**i),k|(1<<i),a+l[i],b))
#                     if a>=(b+l[i]):
#                         dp[ind+2*(3**i)]+=dp[ind]
#                         r.add((ind+2*(3**i),k|(1<<i),a,b+l[i]))
#         que=list(r)
#     return str(res)+'\n'
# # txt=''
# # for t in range(int(input())):
# #     txt+='#'+str(t+1)+' '
# #     txt+=solve()
# # print(txt)

#------------------------------------------------------------#

def permutation(N, weights):
    global result, visited, fac_l, pow_l, total_w
    pow_l = [0]*10
    fac_l = [0]*10
    pow_l[0], fac_l[0] = 1, 1
    for i in range(1, 10):
        pow_l[i] = pow_l[i-1] * 2
        fac_l[i] = fac_l[i-1] * i
    total_w = sum(weights)
    visited = [False] * N
    result = 0
     
    def perm(idx, leftSum, rightSum, remain):
        global N, result, visited, weights, fac_l, pow_l, total_w
        if (leftSum > total_w //2):
            result += (pow_l[N-idx] * fac_l[N-idx])
            return
        if (idx == N):
            result += 1
            return
         
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                cur = weights[i]
                perm(idx+1, leftSum+cur, rightSum, remain-cur)
                if (rightSum + cur <= leftSum):
                    perm(idx+1, leftSum, rightSum+cur, remain-cur)
                visited[i] = False    
    perm(0, 0, 0, total_w)                
    return result
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    answer = permutation(N, weights)
    print("#{} {}".format(t, answer))

N = int(input())
weights = list(map(int, input().split()))
answer = permutation(N, weights)
print(answer)
