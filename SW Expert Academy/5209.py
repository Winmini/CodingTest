INF = int(1e9)


def factory(n, now_cost, k):
    global cost
    if n == k:
        cost = min(cost, now_cost)
        return
    else:
        for i in range(k):
            if visit[i]:
                continue
            if now_cost + board[n][i] >= cost:
                continue
            visit[i] = True
            factory(n+1, now_cost + board[n][i], k)
            visit[i] = False


T = int(input())
for test_case in range(1, T+1):
    cost = INF
    N = int(input())
    visit = [False] * N
    board = []
    for _ in range(N):
        board.append([int(i) for i in input().split()])
    factory(0, 0, N)
    print('#' + str(test_case) + ' ' + str(cost))