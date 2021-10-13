import sys


N = int(input())
c_list = []
for i in range(N):
    tmp = [int(i) for i in sys.stdin.readline().split()] + [i + 1]
    tmp[0] += i
    if tmp[0] <= N:
        c_list.append(tmp)
if c_list:
    dp = [0] * 16
    for end, cost, start in c_list:
        if dp[end]:
            dp[end] = max(dp[end], max(dp[0:start]) + cost)
        else:
            dp[end] = max(max(dp[0:start]) + cost, max(dp[0:end]))
    print(max(dp))
else:
    print(0)