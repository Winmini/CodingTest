import heapq
import sys
INF = int(1e9)


def dijkstra(st):
    distances[st] = 0
    queue = []
    heapq.heappush(queue, (0, st))
    while queue:
        dis, now = heapq.heappop(queue)
        if visited[now] or dis > distances[now]:
            continue
        visited[now] = True
        for i in graph[now]:
            if distances[i[1]] < dis + i[0]:
                continue
            cost = dis + i[0]
            heapq.heappush(queue, (cost, i[1]))
            distances[i[1]] = cost


a = [int(i) for i in sys.stdin.readline().split()]
# 점개수, 간선개수
graph = [[] for _ in range(a[0] + 1)]
visited = [False] * (a[0] + 1)
start = int(input())
# 시작위치
distances = [INF] * (a[0] + 1)
for _ in range(a[1]):
    direction = [int(i) for i in sys.stdin.readline().split()]
    graph[direction[0]].append((direction[2], direction[1]))


dijkstra(start)
for i in distances[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)