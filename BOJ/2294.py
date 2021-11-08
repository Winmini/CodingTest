import sys
from collections import deque
import bisect



n, k = [int(i) for i in sys.stdin.readline().split()]
dp = [0] * (k+1)
coin_set = set()
for _ in range(n):
    c = int(input())
    if c <= k:
        coin_set.add(c)
coin = sorted(list(coin_set))


q = deque([[k, 0]])
while q:
    now, ans = q.popleft()
    if now in coin_set:
        print(ans + 1)
        sys.exit(0)
    tmp = bisect.bisect_left(coin, now)
    for i in range(tmp):
        if dp[now-coin[i]] == 0:
            dp[now-coin[i]] = ans + 1
            q.append([now - coin[i], ans + 1])
print(-1)