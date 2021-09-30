import heapq
import sys
INF = int(1e9)


def dijkstra(st):
    path[st][0] = 0
    queue = []
    heapq.heappush(queue, (0, st))
    while queue:
        cos, now = heapq.heappop(queue)
        if visit[now]:
            continue
        visit[now] = True
        for next_cost, dest in bus[now]:
            if path[dest][0] < cos + next_cost:
                continue
            heapq.heappush(queue, (cos + next_cost, dest))
            path[dest][0] = cos + next_cost
            path[dest][1] = now


vertex = int(input())
edges = int(input())
bus = [[] for _ in range(vertex + 1)]
visit = [False] * (vertex + 1)
path = [[INF, 0] for _ in range(vertex + 1)]

for _ in range(edges):
    start, end, cost = [int(i) for i in sys.stdin.readline().split()]
    bus[start].append([cost, end])

st, ed = [int(i) for i in sys.stdin.readline().split()]
dijkstra(st)
print(path[ed][0])
answer = [ed]
tmp = ed
while tmp != st:
    answer.append(path[tmp][1])
    tmp = path[tmp][1]
print(len(answer))
print(*answer[::-1])
