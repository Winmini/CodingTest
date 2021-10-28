import sys


N, M = [int(i) for i in sys.stdin.readline().split()]
board = []
for _ in range(N):
    board.append([int(i) for i in sys.stdin.readline().split()])

answer = 0
for i in range(M - 3):  # 일자
    for row in board:
        answer = max(answer, sum(row[i:i+4]))

for i in range(N - 3):
    for col in zip(*board):
        answer = max(answer, sum(col[i:i+4]))

for i in range(N - 1):  # 사각형
    for j in range(M - 1):
        answer = max(answer, board[i][j] + board[i+1][j] + board[i][j+1] + board[i+1][j+1])

for i in range(N - 2):
    for j in range(M - 1):
        answer = max(answer, board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1])
        answer = max(answer, board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i][j + 1])
        answer = max(answer, board[i][j+1] + board[i + 1][j+1] + board[i + 2][j+1] + board[i + 2][j])
        answer = max(answer, board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1] + board[i][j])

        answer = max(answer, board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1])
        answer = max(answer, board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j])
        answer = max(answer, board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j])
        answer = max(answer, board[i][j+1] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j+1])

for i in range(N - 1):
    for j in range(M - 2):
        answer = max(answer, sum(board[i][j:j+3]) + board[i+1][j])
        answer = max(answer, sum(board[i][j:j + 3]) + board[i + 1][j+2])
        answer = max(answer, sum(board[i][j:j + 3]) + board[i + 1][j+1])
        answer = max(answer, sum(board[i+1][j:j + 3]) + board[i][j])
        answer = max(answer, sum(board[i+1][j:j + 3]) + board[i][j+2])
        answer = max(answer, sum(board[i+1][j:j + 3]) + board[i][j+1])
        answer = max(answer, sum(board[i][j+1:j + 3]) + sum(board[i+1][j:j+2]))
        answer = max(answer, sum(board[i][j:j + 2]) + sum(board[i + 1][j+1:j + 3]))
print(answer)