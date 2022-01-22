def solution(board, skill):
    imos = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for tp, r1, c1, r2, c2, degree in skill:
        if tp == 1:
            imos[r1][c1] -= degree
            imos[r1][c2+1] += degree
            imos[r2+1][c1] += degree
            imos[r2+1][c2+1] -= degree
        else:
            imos[r1][c1] += degree
            imos[r1][c2+1] -= degree
            imos[r2+1][c1] -= degree
            imos[r2+1][c2+1] += degree


    nxt = 0

    for i in range(len(imos)):
        for j in range(len(imos[0])):
            imos[i][j] += nxt
            nxt = imos[i][j]
    
    nxt = 0
    
    for j in range(len(imos[0])):
        for i in range(len(imos)):
            imos[i][j] += nxt
            nxt = imos[i][j]
    
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + imos[i][j] > 0:
                answer += 1
    
    return answer