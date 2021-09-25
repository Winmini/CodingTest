import heapq
import sys
INF = int(1e9)


def dijkstra(st):
    distances[st] = 0
    queue = []
    heapq.heappush(queue, (0, st))
    while queue:
        dis, now = heapq.heappop(queue)
        if visited[now]:
            continue
        visited[now] = True
        for i in graph[now]:  # i[1] 이 목적지
            if distances[i[1]] < dis + i[0]:
                continue
            cost = dis + i[0]
            heapq.heappush(queue, (cost, i[1]))
            distances[i[1]] = cost

test_case = int(input())

for _ in range(test_case):

    a = [int(i) for i in sys.stdin.readline().split()]
    # 점개수, 간선개수, 목적지 후보개수
    graph = [[] for _ in range(a[0] + 1)]
    drop_by = [int(i) for i in sys.stdin.readline().split()]
    # 출발지, 들러야할곳
    for _ in range(a[1]):
        direction = [int(i) for i in sys.stdin.readline().split()]
        graph[direction[0]].append((direction[2], direction[1]))
        graph[direction[1]].append((direction[2], direction[0]))
    # 양방향 도로
    des_sample = []
    for _ in range(a[2]):
        des_sample.append(int(input()))

    answer = []
    for i in range(3):
        visited = [False] * (a[0] + 1)
        distances = [INF] * (a[0] + 1)
        dijkstra(drop_by[i])
        answer.append(distances[1:])

    first_route = answer[0][drop_by[1]-1] + answer[1][drop_by[2] - 1]
    second_route = answer[0][drop_by[2]-1] + answer[2][drop_by[1] - 1]
    result = []
    if first_route > second_route:
        for i in des_sample:
            if answer[0][i-1] == second_route + answer[1][i-1]:
                result.append(i)
        print(*sorted(result))
    else:
        for i in des_sample:
            if answer[0][i-1] == first_route + answer[2][i-1]:
                result.append(i)
        print(*sorted(result))