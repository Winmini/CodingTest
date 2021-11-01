T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    answer = 0
    visit = [False] * (N + 1)
    apply = [int(i) for i in input().split()]
    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        graph[apply[2*i]].append(apply[2*i + 1])
        graph[apply[2*i + 1]].append(apply[2*i])
    for i in range(1, N+1):
        if visit[i]:
            continue
        q = [i]
        answer += 1
        while q:
            now = q.pop()
            visit[now] = True
            for j in graph[now]:
                if visit[j]:
                    continue
                q.append(j)
    print('#{} {}'.format(test_case, answer))s