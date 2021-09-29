import heapq
import sys
INF = int(1e9)


def dijkstra(st):
    queue = []
    heapq.heappush(queue, (0, st))
    while queue:
        dist, now = heapq.heappop(queue)
        if visited[now]:
            continue
        visited[now] = True
        for now_dist, now_dest in graph[now]:
            if distance[now_dest] < now_dist + dist:
                continue
            dist_update = now_dist + dist
            heapq.heappush(queue, (dist_update, now_dest))
            distance[now_dest] = dist_update


vertex, edges = (int(i) for i in sys.stdin.readline().split())
graph = [[] for _ in range(vertex + 1)]
for _ in range(edges):
    start, dest, dis = (int(i) for i in sys.stdin.readline().split())
    graph[start].append([dis, dest])

answer = []
cnt = [[] for _ in range(vertex + 1)]
# 돌아갈 수 없는 곳 체크
for i in range(1, vertex + 1):
    visited = [False] * (vertex + 1)
    for idx, j in enumerate(cnt):
        if i in j:
            visited[idx] = True
    distance = [INF] * (vertex + 1)
    dijkstra(i)
    for idx, j in enumerate(distance):
        if j == INF:
            cnt[i].append(idx)
    answer.append(distance[i])
if min(answer) == INF:
    print(-1)
else:
    print(min(answer))