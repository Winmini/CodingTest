import sys


dir_x = [-1, -1, -1, 0, 0, 1, 1, 1]
dir_y = [0, 1, -1, 1, -1, 0, -1, 1]


N, M, K = [int(i) for i in sys.stdin.readline().split()]
answer = 0
food = []
board = [[5] * N for _ in range(N)]
Trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(N):
    food.append([int(i) for i in sys.stdin.readline().split()])
for _ in range(M):
    x, y, z = [int(i) for i in sys.stdin.readline().split()]
    Trees[x-1][y-1].append(z)


for idx in range(N):
    for idy in range(N):
        Trees[idx][idy].sort()

for _ in range(K):
    for idx in range(N):
        for idy in range(N):
            Trees[idx][idy].sort()
            for tree, age in enumerate(Trees[idx][idy]):
                if age <= board[idx][idy]:
                    Trees[idx][idy][tree] += 1
                    board[idx][idy] -= age
                else:
                    board[idx][idy] += sum([i//2 for i in Trees[idx][idy][tree:]])
                    Trees[idx][idy] = Trees[idx][idy][:tree]
                    break

    for idx in range(N):
        for idy in range(N):
            for i in Trees[idx][idy]:
                if i % 5 == 0:
                    for i in range(8):
                        cur_x = idx + dir_x[i]
                        cur_y = idy + dir_y[i]
                        if cur_x < 0 or cur_y < 0 or cur_x == N or cur_y == N:
                            continue
                        Trees[cur_x][cur_y].append(1)

    for idx in range(N):
        for idy in range(N):
            board[idx][idy] += food[idx][idy]

for idx in range(N):
    for idy in range(N):
        answer += len(Trees[idx][idy])
print(answer)