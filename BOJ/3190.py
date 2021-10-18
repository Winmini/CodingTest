from collections import deque
import sys


N = int(sys.stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]
board[0][0] = 1

K = int(sys.stdin.readline())
for _ in range(K):
    x, y = [int(i) for i in sys.stdin.readline().split()]
    board[x - 1][y - 1] = 2

L = int(sys.stdin.readline())
snake_dir = deque()  # 3시방향, 오른쪽
for _ in range(L):
    snake_dir.append([i for i in sys.stdin.readline().split()])

snake = deque([[0, 0]])
time = 0
t_dir = 3

while True:
    time += 1
    now_dir = t_dir
    now_x, now_y = snake[-1]
    if t_dir == 3:
        now_y += 1
    elif t_dir == 6:
        now_x += 1
    elif t_dir == 9:
        now_y -= 1
    elif t_dir == 0:
        now_x -= 1

    if now_x < 0 or now_y < 0 or now_x >= N or now_y >= N or board[now_x][now_y] == 1:
        print(time)
        break

    if board[now_x][now_y] == 2:
        board[now_x][now_y] = 1
        snake.append([now_x, now_y])
    elif board[now_x][now_y] == 0:
        snake.append([now_x, now_y])
        board[now_x][now_y] = 1
        p_x, p_y = snake.popleft()
        board[p_x][p_y] = 0
    if snake_dir:
        if int(snake_dir[0][0]) <= time:
            n_dir = snake_dir.popleft()
            if t_dir == 3:
                if n_dir[1] == 'L':
                    t_dir = 0
                else:
                    t_dir = 6
            elif t_dir == 6:
                if n_dir[1] == 'L':
                    t_dir = 3
                else:
                    t_dir = 9
            elif t_dir == 9:
                if n_dir[1] == 'L':
                    t_dir = 6
                else:
                    t_dir = 0
            elif t_dir == 0:
                if n_dir[1] == 'L':
                    t_dir = 9
                else:
                    t_dir = 3

