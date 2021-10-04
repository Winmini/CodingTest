import sys

INF = int(1e9)


def dfs(st):
    q = [st]
    while q:
        now = q.pop()
        visit[now] = True
        for next_d, next_v in graph[now]:
            if visit[next_v]:
                continue
            answer[next_v] = answer[now] + next_d
            q.append(next_v)


vertex = int(input())
graph = [[] for _ in range(vertex + 1)]
visit = [False] * (vertex + 1)

for _ in range(vertex - 1):
    start, end, dist = [int(i) for i in sys.stdin.readline().split()]
    graph[start].append([dist, end])
    graph[end].append([dist, start])

answer = [0] * (vertex + 1)
dfs(1)
idx = answer.index(max(answer))
visit = [False] * (vertex + 1)
answer = [0] * (vertex + 1)
dfs(idx)
print(max(answer))