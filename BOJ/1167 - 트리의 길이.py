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

for _ in range(vertex):
    info = [int(i) for i in sys.stdin.readline().split()]
    for i in range((len(info) - 2) // 2):
        graph[info[0]].append(info[1 + 2 * i: 3 + 2 * i][::-1])

answer = [0] * (vertex + 1)
for i in range(1, vertex + 1):
    if len(graph[i]) == 1:
        dfs(i)
        break

idx = answer.index(max(answer))
visit = [False] * (vertex + 1)
answer = [0] * (vertex + 1)
dfs(idx)
print(max(answer))