import heapq


INF = int(1e9)


def solution(n, s, a, b, fares):
    answer = INF
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)
    for st, ed, fare in fares:
        graph[st].append([fare, ed])
        graph[ed].append([fare, st])
    

    def dijkstra(st):
        distance[st] = 0
        queue = []
        heapq.heappush(queue, [0, st])
        while queue:
            dist, now = heapq.heappop(queue)
            visited[now] = True
            for nextDist, nextDest in graph[now]:
                if visited[nextDest]:
                    continue
                if distance[nextDest] < dist + nextDist:
                    continue
                updateDist = dist + nextDist
                heapq.heappush(queue, [updateDist, nextDest])
                distance[nextDest] = updateDist
    dijkstra(s)
    midDistance = distance[:]
    
    for i in range(1, n+1):
        visited = [False] * (n + 1)
        distance = [INF] * (n + 1)
        dijkstra(i)
        answer = min(answer, midDistance[i] + distance[a] + distance[b])
    
    return answer