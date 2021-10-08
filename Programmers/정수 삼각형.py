def solution(triangle)
    dp = [[0]  i for i in range(1, (len(triangle) + 1))]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle))
        for j in range(len(dp[i]))
            if j == 0
                dp[i][0] = dp[i-1][0] + triangle[i][j]
            elif j == len(dp[i])-1
                dp[i][-1] = dp[i-1][-1] + triangle[i][j]
            else
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    return max(dp[-1])