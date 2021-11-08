import sys

T = int(input())
for _ in range(T):
    col = int(input())
    sticker = [[int(i) for i in sys.stdin.readline().split()], [int(i) for i in sys.stdin.readline().split()]]
    dp = [[0] * col for _ in range(2)]
    if col == 1:
        print(max(sticker[0][0], sticker[1][0]))
    else:
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]
        for i in range(2, col):
            dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + sticker[0][i]
            dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + sticker[1][i]
        print(max(dp[0][-1], dp[1][-1]))