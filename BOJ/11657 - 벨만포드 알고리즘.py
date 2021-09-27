import sys
INF = int(1e9)


def bf(st):
    distances[st] = 0
    for i in range(a[0]):
        for j in range(a[1]):
            cur = graph[j][0]
            next_node = graph[j][1]
            cost = graph[j][2]
            if distances[cur] != INF and distances[next_node] > distances[cur] + cost:
                distances[next_node] = distances[cur] + cost
                if i == a[0] - 1:
                    return True
    return False


a = [int(i) for i in sys.stdin.readline().split()]
# 점개수, 간선개수
graph = []
visited = [False] * (a[0] + 1)
distances = [INF] * (a[0] + 1)
# 출발지, 들러야할곳
for _ in range(a[1]):
    direction = [int(i) for i in sys.stdin.readline().split()]
    graph.append((direction[0], direction[1], direction[2]))


result = bf(1)

if result:
    print('-1')
else:
    for i in distances[2:]:
        if i == INF:
            print('-1')
        else:
            print(i)