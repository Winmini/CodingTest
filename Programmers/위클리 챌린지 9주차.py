def solution(n, wires):
    answer = []
    for i in range(len(wires)):
        wire = wires[0:i] + wires[i+1:]
        graph = [[] for _ in range(n+1)]
        visit = [False] * (n+1)
        for x, y in wire:
            graph[x].append(y)
            graph[y].append(x)
        cnt = 0
        q = [1]
        while q:
            now = q.pop()
            cnt += 1
            if visit[now]:
                continue
            visit[now] = True
            for j in graph[now]:
                if visit[j]:
                    continue
                q.append(j)
        answer.append(abs(n - 2*cnt))
    return min(answer)