import sys


def dfs(start):
    visit[start] = True
    for i in adj[start]:
        if not visit[i]:
            dfs(i)


com = int(sys.stdin.readline())
con = int(sys.stdin.readline())


adj = [[] for _ in range(com + 1)]
visit = [False] * (com + 1)

for _ in range(con):
    tmp = [int(i) for i in sys.stdin.readline().split()]
    adj[tmp[0]].append(tmp[1])
    adj[tmp[1]].append(tmp[0])

dfs(1)
answer = 0
for i in visit:
    if i:
        answer+=1
print(answer - 1)
