import sys

result = 1


def dfs(now_x, now_y, answer):
    global result
    result = max(answer, result)
    for i in range(4):
        cur_x = now_x + dir_x[i]
        cur_y = now_y + dir_y[i]
        if 0 <= cur_x < R and 0 <= cur_y < C and board[cur_x][cur_y] not in alphabet:
            alphabet.append(board[cur_x][cur_y])
            dfs(cur_x, cur_y, answer + 1)
            alphabet.remove(board[cur_x][cur_y])


dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]
R, C = [int(i) for i in sys.stdin.readline().split()]
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
alphabet = [board[0][0]]
dfs(0, 0, 1)
print(result)