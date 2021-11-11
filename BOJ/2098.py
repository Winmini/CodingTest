import sys
INF = int(1e9)


def tour_city(now, visit):
    if visit == (1 << N) -1:
        return city[now][0] or INF
    if dp[now][visit]:
        return dp[now][visit]
    tmp = INF
    for c in range(N):
        if visit & (1 << c) == 0 and city[now][c]:
            tmp = min(tmp, tour_city(c, visit | (1 << c)) + city[now][c])
    dp[now][visit] = tmp
    return tmp


N = int(input())
dp = [[None] * (1 << N) for _ in range(N)]
city = [[] for _ in range(N)]
for i in range(N):
    row = [int(i) for i in sys.stdin.readline().split()]
    for idx, j in enumerate(row):
        city[idx].append(j)

print(tour_city(0, 1 << 0))