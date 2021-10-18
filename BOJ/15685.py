import sys


board = [[False] * 101 for _ in range(101)]
N = int(sys.stdin.readline())
dragon = []
for _ in range(N):
    dragon.append([int(i) for i in sys.stdin.readline().split()])

for x, y, d, g in dragon:
    board[y][x] = True
    dp = [[] for _ in range(g + 1)]
    if d == 0:
        x += 1
        dp[0].append([x, y, d])
    elif d == 1:
        y -= 1
        dp[0].append([x, y, d])
    elif d == 2:
        x -= 1
        dp[0].append([x, y, d])
    elif d == 3:
        y += 1
        dp[0].append([x, y+1, d])
    board[y][x] = True
    for i in range(1, g + 1):
        for j in range(i-1, -1, -1):
            for k in dp[j][::-1]:
                # 0: 오른쪽, 1: 위쪽, 2: 왼쪽, 3: 아래쪽
                if k[2] == 0:
                    y -= 1
                    dp[i].append([x, y, 1])
                elif k[2] == 1:
                    x -= 1
                    dp[i].append([x, y, 2])
                elif k[2] == 2:
                    y += 1
                    dp[i].append([x, y, 3])
                elif k[2] == 3:
                    x += 1
                    dp[i].append([x, y, 0])
                board[y][x] = True

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] == True:
            answer += 1
print(answer)
