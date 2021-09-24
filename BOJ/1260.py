import sys
import heapq


def dfs(start):
    print(start, end=' ')
    visit[start] = True
    for i in adj[start]:
        if not visit[i]:
            dfs(i)


a = [int(i) for i in sys.stdin.readline().split()]
adj = [[] for _ in range(a[0] + 1)]
visit = [False] * (a[0] + 1)

for _ in range(a[1]):
    tmp = [int(i) for i in sys.stdin.readline().split()]
    adj[tmp[0]].append(tmp[1])
    adj[tmp[1]].append(tmp[0])

for i in adj:
    i.sort()

q = [a[2]]
dfs(a[2])
print()
visit = [False] * (a[0] + 1)
while q:
    cur = q.pop(0)
    if not visit[cur]:
        visit[cur] = True
        print(cur, end=' ')
        for i in adj[cur]:
            if not visit[i]:
                q.append(i)