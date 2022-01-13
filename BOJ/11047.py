import bisect
import sys


N, K = [int(i) for i in sys.stdin.readline().split()]
coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline().split()[0]))
coin.sort()
loc = bisect.bisect_right(coin, K) - 1
answer = 0
while K != 0:
    answer += K // coin[loc]
    K -= K // coin[loc] * coin[loc]
    loc = bisect.bisect_right(coin, K) - 1
print(answer)