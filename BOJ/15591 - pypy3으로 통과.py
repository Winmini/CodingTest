import sys
INF = int(1e9) + 1

N, Q = [int(i) for i in sys.stdin.readline().split()]
graph = [[] for _ in range(N+1)]


for _ in range(N - 1):
    p, q, r = [int(i) for i in sys.stdin.readline().split()]
    graph[p].append([r, q])
    graph[q].append([r, p])
for _ in range(Q):
    visit = [False for _ in range(N + 1)]
    k, v = [int(i) for i in sys.stdin.readline().split()]
    q = [[INF, v]]
    dist = [0] * (N + 1)
    while q:
        cost, now = q.pop()
        visit[now] = True
        for c, n in graph[now]:
            if visit[n]:
                continue
            dist[n] = min(c, cost)
            q.append([dist[n], n])
    print(sum([True for i in dist[1:] if i >= k]))