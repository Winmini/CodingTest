import bisect
import sys


a = int(input())
seq = [int(i) for i in sys.stdin.readline().split()]
lis = [seq[0]]
ans = 1
dp = [0] * a
for idx, num in enumerate(seq[1:]):
    if lis[-1] < num:
        lis.append(num)
        ans += 1
    else:
        lis[bisect.bisect_left(lis, num)] = num
    dp[idx + 1] = bisect.bisect_left(lis, num)
print(ans)
result = []
for i in range(a - 1, -1, -1):
    if dp[i] == ans - 1:
        result.append(seq[i])
        ans -= 1
print(*result[::-1])