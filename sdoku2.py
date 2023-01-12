import sys
sys.stdin = open("input.txt","r")
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    # 가로 세로 검사
    for i in range(9):
        cnt_r = [0] * 10
        cnt_c = [0] * 10
        for j in range(9):
            cnt_r[arr[i][j]] += 1
            cnt_c[arr[j][i]] += 1

        # 중복 체크
        for k in range(1, 10):
            if cnt_r[k] != 1:
                result = 0
                break
            if cnt_c[k] != 1:
                result = 0
                break

    # 3x3 격자 검사
    for i in range(3):
        for j in range(3):
            cnt_x = [0] * 10
            for k in range(3):
                for l in range(3):
                    cnt_x[arr[3*i+k][3*j+l]] += 1

            for k in range(1, 10):
                if cnt_x[k] != 1:
                    result = 0
                    break

    print("#{} {}".format(tc, result))