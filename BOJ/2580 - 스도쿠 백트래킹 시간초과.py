import sys


a = []
board1 = [[0 for col in range(10)] for row in range(9)]  # 가로
board2 = [[0 for col in range(10)] for row in range(9)]  # 세로
board3 = [[0 for col in range(10)] for row in range(9)]  # 사각형


for i in range(9):
    tmp = [int(i) for i in sys.stdin.readline().split()]
    a.append(tmp)
    for idx, j in enumerate(tmp):
        board1[i][j] = 1
        board2[idx][j] = 1
    if i <= 2:
        for j in range(3):
            board3[0][tmp[j]] = 1
            board3[1][tmp[j+3]] = 1
            board3[2][tmp[j+6]] = 1
    elif i <= 5:
        for j in range(3):
            board3[3][tmp[j]] = 1
            board3[4][tmp[j+3]] = 1
            board3[5][tmp[j+6]] = 1
    else:
        for j in range(3):
            board3[6][tmp[j]] = 1
            board3[7][tmp[j+3]] = 1
            board3[8][tmp[j+6]] = 1
chk_zero = [(i, j) for i in range(9) for j in range(9) if not a[i][j]]


def sdoku(chk):
    if chk == len(chk_zero):
        for i in a:
            print(*i)
        sys.exit(0)
    else:
        for i in range(1,10):
            idx = chk_zero[chk][0]
            idy = chk_zero[chk][1]
            if not board1[idx][i]:
                if not board2[idy][i]:
                    if not board3[(idx//3)*3 + idy//3][i]:
                        a[idx][idy] = i
                        board1[idx][i] = 1
                        board2[idy][i] = 1
                        board3[(idx // 3) * 3 + idy // 3][i] = 1
                        sdoku(chk + 1)
                        a[idx][idy] = 0
                        board1[idx][i] = 0
                        board2[idy][i] = 0
                        board3[(idx // 3) * 3 + idy // 3][i] = 0


sdoku(0)