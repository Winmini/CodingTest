from collections import deque


def bfs(q):
    while q:
        now, num = q.popleft()
        for i in (now + 1, now - 1, now*2, now - 10):
            if 0 < i <= 1000000 and not chk.get(i, 0):
                q.append((i, num + 1))
                chk[i] = 1
                if i == M:
                    return num + 1


T = int(input())
for test_case in range(1, T+1):
    chk = {}
    N, M = map(int, input().split())
    Q = deque()
    Q.append((N, 0))
    chk[N] = 1
    print('#{} {}'.format(test_case, bfs(Q)))