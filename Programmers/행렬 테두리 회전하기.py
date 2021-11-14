def solution(rows, columns, queries):
    board = [[i + columns * j for i in range(1,columns+1)] for j in range(rows)]
    answer = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        min_move = int(1e9)
        tmp1 = board[x1][y2]
        tmp2 = board[x2][y1]
        tmp3 = board[x2][y2]
        min_move = min(min_move, tmp1, tmp2, tmp3)
        for i in range(y2-y1):
            board[x1][y2 - i] = board[x1][y2 - i - 1]
            min_move =  min(min_move,board[x1][y2 - i])
        for i in range(x2-x1):
            board[x2 - i][y2] = board[x2 - i - 1][y2]
            min_move =  min(min_move,board[x2 - i][y2])
        for i in range(y2-y1):
            board[x2][y1 + i] = board[x2][y1 + i + 1]
            min_move =  min(min_move,board[x2][y1 + i])
        for i in range(x2-x1):
            board[x1 + i][y1] = board[x1 + i + 1][y1]
            min_move =  min(min_move,board[x1 + i][y1])
        answer.append(min_move)
        board[x1+1][y2] = tmp1
        board[x2][y2-1] = tmp3
        board[x2-1][y1] = tmp2
        
    return answer