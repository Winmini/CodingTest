from collections import deque
import sys


dir_x = [0, 0, 1, -1]
dir_y = [-1, 1, 0, 0]

N, L, R = [int(i) for i in sys.stdin.readline().split()]
board = []


for _ in range(N):
    board.append([int(i) for i in sys.stdin.readline().split()])


answer = 0

while True:
    trade = []
    trade_people = []
    visit = [[False] * N for _ in range(N)]
    for idx, row in enumerate(board):
        for idy, col in enumerate(row):
            tmp = []
            people_num = 0
            if visit[idx][idy]:
                continue
            visit[idx][idy] = True
            people_num += board[idx][idy]
            q = deque([[idx, idy]])
            while q:
                now_x, now_y = q.pop()
                tmp.append([now_x, now_y])
                for i in range(4):
                    cur_x = now_x + dir_x[i]
                    cur_y = now_y + dir_y[i]
                    if cur_x < 0 or cur_y < 0 or cur_x == N or cur_y == N:
                        continue
                    if visit[cur_x][cur_y]:
                        continue
                    if L <= abs(board[now_x][now_y] - board[cur_x][cur_y]) <= R:
                        q.append([cur_x, cur_y])
                        people_num += board[cur_x][cur_y]
                        visit[cur_x][cur_y] = True
            if len(tmp) > 1:
                trade.append(tmp)
                trade_people.append(people_num)
    if not trade:
        break
    for i, country in enumerate(trade):
        for x, y in country:
            board[x][y] = trade_people[i] // len(country)
    answer += 1
print(answer)