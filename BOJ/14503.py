import sys


dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


R, C = [int(i) for i in sys.stdin.readline().split()]
visit = [[False for _ in range(C)] for _ in range(R)]
q = [[int(i) for i in sys.stdin.readline().split()]]
board = []
for _ in range(R):
    board.append([int(i) for i in sys.stdin.readline().split()])

while q:
    now_x, now_y, dt = q.pop()
    cur_x, cur_y = 0, 0
    visit[now_x][now_y] = True
    chk = 1
    for _ in range(4):
        if dt == 0:
            cur_x = now_x
            cur_y = now_y - 1
            dt = 3
        elif dt == 1:
            cur_x = now_x - 1
            cur_y = now_y
            dt = 0
        elif dt == 2:
            cur_x = now_x
            cur_y = now_y + 1
            dt = 1
        else:  # dt = 3
            cur_x = now_x + 1
            cur_y = now_y
            dt = 2
        if board[cur_x][cur_y] != 1 and not visit[cur_x][cur_y]:
            chk = 0
            break
    if chk:
        if dt == 0 and board[now_x+1][now_y] != 1:
            q.append([now_x+1, now_y, dt])
        elif dt == 1 and board[now_x][now_y-1] != 1:
            q.append([now_x, now_y-1, dt])
        elif dt == 2 and board[now_x-1][now_y] != 1:
            q.append([now_x-1, now_y, dt])
        elif dt == 3 and board[now_x][now_y+1] != 1:
            q.append([now_x, now_y+1, dt])
    else:
        q.append([cur_x, cur_y, dt])

answer = 0
for i in visit:
    answer += sum(i)
print(answer)