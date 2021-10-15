import sys


def bk(n, state, num):
    global L
    if n + 1 == len(row): # 감소 여분남았다면 실패
        if state:
            return
        else:
            global answer
            answer += 1
    else:
        if row[n] == row[n+1]:
            if state > 0:
                bk(n+1, state-1, 0)
            else:
                bk(n+1, 0, num+1)
        elif row[n] - row[n+1] == 1:  # 감소
            if state > 0:
                return
            else:
                bk(n+1, L - 1, 0)
        elif row[n] - row[n+1] == -1: # 증가
            if num >= L:
                bk(n+1, 0, 1)
            else:
                return 0
        else:
            return 0


N, L = [int(i) for i in sys.stdin.readline().split()]
visit = [[False for _ in range(N)] for _ in range(N)]
board = []
for _ in range(N):
    board.append([int(i) for i in sys.stdin.readline().split()])
answer = 0
for row in board:
    bk(0, 0, 1)
for row in zip(*board):
    bk(0, 0, 1)
print(answer)