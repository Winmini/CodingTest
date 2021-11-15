def solution(m, n, puddles):
    # n은 행, m은 열

    dp = [[0] * m for _ in range(n)]

    if puddles != [[]]: 
        for c, r in puddles:
            dp[r-1][c-1] = -1

    if dp[0][1] != -1:
        for c in range(1, m):
            if dp[0][c-1] != -1 and dp[0][c] != -1:
                dp[0][c] = 1
            else:
                dp[0][c] = -1
    
    if dp[1][0] != -1:
        for r in range(1, n):
            if dp[r-1][0] != -1 and dp[r][0] != -1:
                dp[r][0] = 1
            else:
                dp[r][0] = -1

    for c in range(1, m):
        for r in range(1, n):
            if dp[r][c] != -1:
                if dp[r-1][c] != -1 and dp[r][c-1] != -1:    
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
                elif dp[r-1][c] != -1 and dp[r][c-1] == -1:
                    dp[r][c] = dp[r-1][c]
                elif dp[r-1][c] == -1 and dp[r][c-1] != -1:
                    dp[r][c] = dp[r][c-1]
                dp[r][c] %= 1000000007

    return dp[n-1][m-1]