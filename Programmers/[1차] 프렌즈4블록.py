def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    chk = True
    while(chk):
        chk = False
        erase = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '0':
                    if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                        erase.add((i,j))
                        erase.add((i+1,j))
                        erase.add((i,j+1))
                        erase.add((i+1,j+1))
                        chk = True
        for i, j in sorted(list(erase)):
            answer += 1
            k = 1
            while(i - k != -1):
                board[i-k+1][j] = board[i-k][j]
                k += 1
            board[0][j] = '0'

    return answer