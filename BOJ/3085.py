dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))

answer = 0
for now_x in range(N):
    for now_y in range(N):
        for i in range(4):
            cur_x = now_x + dir_x[i]
            cur_y = now_y + dir_y[i]
            if 0 <= cur_x < N and 0 <= cur_y < N:
                row_num = 1
                col_num = 1
                board[now_x][now_y], board[cur_x][cur_y] = board[cur_x][cur_y], board[now_x][now_y]
                row = 1
                while cur_x + row < N and board[cur_x][cur_y] == board[cur_x + row][cur_y]:
                    row += 1
                row_num += row - 1
                row = 1
                while cur_x - row >= 0 and board[cur_x][cur_y] == board[cur_x - row][cur_y]:
                    row += 1
                row_num += row - 1
                col = 1
                while cur_y + col < N and board[cur_x][cur_y] == board[cur_x][cur_y + col]:
                    col += 1
                col_num += col - 1
                col = 1
                while cur_y - col >= 0 and board[cur_x][cur_y] == board[cur_x][cur_y - col]:
                    col += 1
                col_num += col - 1
                answer = max(answer, row_num, col_num)
                board[now_x][now_y], board[cur_x][cur_y] = board[cur_x][cur_y], board[now_x][now_y]
print(answer)