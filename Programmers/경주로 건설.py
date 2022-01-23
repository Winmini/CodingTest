from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def solution(board):
    def bfs(x,y,cost,d):
        n = len(board)
        result = [[int(1e9) for _ in range(n)] for _ in range(n)]
        q = deque()
        q.append((x,y,cost,d))
        result[x][y] = 0
        while q:
            x,y,cost,d = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                ncost = cost + 600 if i != d else cost + 100
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and result[nx][ny] > ncost:
                    result[nx][ny] = ncost
                    q.append((nx,ny,ncost,i))
        return result[-1][-1]
    return min(bfs(0,0,0,0),bfs(0,0,0,2))