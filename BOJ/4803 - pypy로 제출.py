import sys


case = 1
while True:
    N, M = [int(i) for i in sys.stdin.readline().split()]
    graph = [[] for _ in range(N + 1)]
    visit = [False] * (N + 1)
    answer = 0
    if N:
        for _ in range(M):
            i, j = [int(i) for i in sys.stdin.readline().split()]
            graph[i].append(j)
            graph[j].append(i)
        for i in range(1, N+1):
            if not visit[i]:
                answer += 1
                tmp = 0
                q = [[i, 0]]
                while q:
                    now, before = q.pop()
                    visit[now] = True
                    for g in graph[now]:
                        if g == before:
                            continue
                        if visit[g]:
                            tmp = 1
                            continue
                        q.append([g, now])
                if tmp:
                    answer -= 1
        if answer == 1:
            print('Case {}: There is one tree.'.format(case))
        elif answer > 1:
            print('Case {}: A forest of {} trees.'.format(case, answer))
        else:
            print('Case {}: No trees.'.format(case))
        case += 1
    else:
        break