from collections import deque
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


for _ in range(edges):
    start, end, cost = [int(i) for i in sys.stdin.readline().split()]
    bus[start].append([cost, end])

answer = []
for v in range(1, vertex+1):
    path = [[INF, 0] for _ in range(vertex + 1)]
    visit = [False] * (vertex + 1)
    dijkstra(v)
    answer.append(path[1:])

for i in range(vertex):
    for j in range(vertex):
        if answer[i][j][0] == INF:
            answer[i][j][0] = 0

for i in answer:
    for j in (zip(*i)):
        print(*j)
        break

for i in answer:
    for idx, j in enumerate(i):
        if j[0] == 0:
            print(0)
        else:
            tmp = deque([idx + 1])
            while tmp[0] != 0:
                tmp.appendleft(i[tmp[0]-1][1])
            tmp[0] = len(tmp) - 1
            print(*tmp)