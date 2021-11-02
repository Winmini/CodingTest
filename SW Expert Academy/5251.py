import heapq


INF = int(1e9)
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


T = int(input())
for test_case in range(1, T + 1):
    v, e = [int(i) for i in input().split()]
    visit = [False] * (v+1)
    dist = [INF] * (v+1)
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        st, ed, ct = [int(i) for i in input().split()]
        graph[st].append([ct, ed])
    dist[0] = 0
    q = []
    heapq.heappush(q, (0, 0))
    while q:
        dis, now = heapq.heappop(q)
        if visit[now]:
            continue
        visit[now] = True
        for i in graph[now]:
            if dist[i[1]] < i[0] + dis:
                continue
            heapq.heappush(q, (dis + i[0], i[1]))
            dist[i[1]] = dis + i[0]
    print('#{} {}'.format(test_case, dist[v]))