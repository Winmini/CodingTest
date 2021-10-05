import heapq



def solution(n, edge):
    INF = int(1e9)
    vertex = n
    graph = [[] for _ in range(vertex + 1)]
    dist = [INF] * (vertex + 1)

    visit = [False] * (vertex + 1)
    for start, end in edge:
        graph[start].append([1, end])
        graph[end].append([1, start])
        
        
    st = 1
    dist[st] = 0
    queue = []
    heapq.heappush(queue, (0, st))
    while queue:
        now_dist, now = heapq.heappop(queue)
        if visit[now]:
            continue
        visit[now] = True
        for next_dist, next_node in graph[now]:
            if dist[next_node] < next_dist + now_dist:
                continue
            heapq.heappush(queue, (next_dist + now_dist, next_node))
            dist[next_node] = next_dist + now_dist
    answer = dist[1:].count(max(dist[1:]))
    return answer