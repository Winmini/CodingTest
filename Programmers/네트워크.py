def solution(n, computers):
    visit = [False] * (n+1)
    graph = [[] for _ in range(n + 1)]
    for st, com in enumerate(computers):
        for ed, i in enumerate(com):
            if i and st != ed:
                graph[st + 1].append(ed + 1)
    answer = -1   
    for st, i in enumerate(graph):
        if i and not visit[st]:
            q = [st]
            while q:
                now = q.pop()
                visit[now] = True
                for i in graph[now]:
                    if visit[i]:
                        continue
                    q.append(i)  
            answer += 1
        if not i:
            answer += 1

    return answer