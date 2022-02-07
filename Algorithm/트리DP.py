import sys
sys.setrecursionlimit(10**6)


def recursive_dp(num):
    visited[num] = True
    dp[num][0] = 0
    dp[num][1] = 1
    for children in graph[num]:
        if visited[children]:
            continue
        recursive_dp(children)
        dp[num][0] += dp[children][1]
        dp[num][1] += min(dp[children][0], dp[children][1])


N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
dp = [[0, 0] for _ in range(N+1)]
for _ in range(N - 1):
    i, j = [int(i) for i in sys.stdin.readline().split()]
    graph[i].append(j)
    graph[j].append(i)

recursive_dp(1)
print(min(dp[1]))