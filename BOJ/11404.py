import heapq
import sys
INF = int(1e9)


def dijkstra(st):
    distances[st] = 0
    queue = []
    heapq.heappush(queue, (0, st))
    while queue:
        cost, now = heapq.heappop(queue)
        if visited[now]:
            continue
        visited[now] = True
        for i in graph[now]:
            if distances[i[1]] < i[0] + cost:
                continue
            n_cost = i[0] + cost
            heapq.heappush(queue, (n_cost, i[1]))
            distances[i[1]] = n_cost


node = int(input())
edges = int(input())
a = [node, edges]
# 점개수, 간선개수
graph = [[] for _ in range(a[0] + 1)]
visited = [False] * (a[0] + 1)
distances = [INF] * (a[0] + 1)
# 출발지, 들러야할곳
for _ in range(a[1]):
    direction = [int(i) for i in sys.stdin.readline().split()]
    graph[direction[0]].append([direction[2], direction[1]])

for i in range(1, a[0] + 1):
    visited = [False] * (a[0] + 1)
    distances = [INF] * (a[0] + 1)
    dijkstra(i)
    for j in distances[1:]:
        if j == INF:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()