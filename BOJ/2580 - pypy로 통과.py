import sys


def dfs(n):
    if n == -1:
        for i in sdoku:
            print(*i)
        sys.exit(0)
    r, c = searchList[n]
    for i in range(1, 10):
        if not rowVisit[r][i]:
            if not colVisit[c][i]:
                if not squareVisit[r // 3][c // 3][i]:
                    rowVisit[r][i] = True
                    colVisit[c][i] = True
                    squareVisit[r//3][c//3][i] = True
                    sdoku[r][c] = i
                    dfs(n-1)
                    rowVisit[r][i] = False
                    colVisit[c][i] = False
                    squareVisit[r//3][c//3][i] = False
                    sdoku[r][c] = 0


sdoku = []
for _ in range(9):
    sdoku.append([int(i) for i in sys.stdin.readline().split()])

rowVisit = [[False] * 10 for _ in range(9)]
for idx, row in enumerate(sdoku):
    for i in row:
        rowVisit[idx][i] = True

colVisit = [[False] * 10 for _ in range(9)]
for idx, col in enumerate(zip(*sdoku)):
    for i in col:
        colVisit[idx][i] = True

squareVisit = [[[False] * 10 for _ in range(3)] for _ in range(3)]
for i in range(9):
    for j in range(9):
        squareVisit[i // 3][j // 3][sdoku[i][j]] = True

searchList = []
for i in range(9):
    for j in range(9):
        if not sdoku[i][j]:
            searchList.append([i, j])

dfs(len(searchList) - 1)