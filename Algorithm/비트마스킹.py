l = [-1] * 20
r = [-1] * 20
vis = [False] * (1 << 17)
inf = []
ans = 0
n = 0


def solve(state):
    global ans
    if vis[state]:
        return
    vis[state] = True
    wolf = 0
    num = 0
    for i in range(n):
        if state & (1 << i):
            wolf += inf[i]
            num += 1
    if wolf*2 >= num:
        return
    ans = max(ans, num - wolf)
    for i in range(n):
        if not state & (1 << i):
            continue
        if l[i] != -1:
            solve(state | (1<<l[i]))
        if r[i] != -1:
            solve(state | (1<<r[i]))

            
def solution(info, edges):
    global ans, n, inf
    n = len(info)
    inf = info[:]
    for i, j in edges:
        if l[i] == -1:
            l[i] = j
        else:
            r[i] = j
    solve(1)
    return ans
