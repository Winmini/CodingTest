T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    dp = [[0] * N for _ in range(N)]
    board = []
    for _ in range(N):
        board.append([int(i) for i in input().split()])
    dp[0][0] = board[0][0]
    for i in range(1, N):
        for j in range(i + 1):
            dp[0][i] += board[0][j]
            dp[i][0] += board[j][0]
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + board[i][j]
    print("#" + str(test_case) + " " + str(dp[N-1][N-1]))