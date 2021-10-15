from itertools import combinations
import sys



N, M, H = [int(i) for i in sys.stdin.readline().split()]
graph = [[] for _ in range(N + 1)]
all_line = [[n, h] for n in range(1, N) for h in range(1, H+1)]
for _ in range(M):
    a, b = [int(i) for i in sys.stdin.readline().split()]
    graph[b].append([a, b+1])
    graph[b+1].append([a, b])
    if [b, a] in all_line:
        all_line.remove([b, a])
    if [b+1, a] in all_line:
        all_line.remove([b+1, a])
    if [b-1, a] in all_line:
        all_line.remove([b-1, a])

for n in range(4):
    add_line = list(combinations(all_line, n))
    for lines in add_line:
        t_graph = [item[:] for item in graph]
        for b, a in lines:
            t_graph[b].append([a, b+1])
            t_graph[b+1].append([a, b])
        for idx, s in enumerate(t_graph):
            t_graph[idx] = sorted(s)
        for i in range(1, N+1):
            q = [[i, 0]]
            tmp = 0
            while q:
                now, h = q.pop()
                tmp = now

                for H, nt in t_graph[now]:
                    if H <= h:
                        continue
                    q.append([nt, H])
                    break
            if tmp != i:
                break
            if tmp == i == N:
                print(n)
                sys.exit(0)
print(-1)