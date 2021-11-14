from collections import deque


dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]
def solution(maps):
    col = len(maps[0])
    row = len(maps)
    visit = [[False] * col for _ in range(row)]
    visit[0][0] = True
    q = deque([[0, 0, 1]])
    answer = -1
    while q:
        now_x, now_y, cnt = q.popleft()
        if now_x == row-1 and now_y == col-1:
            answer = cnt
            break
        for i in range(4):
            cur_x = now_x + dir_x[i]
            cur_y = now_y + dir_y[i]
            if cur_x < 0 or cur_y < 0 or cur_x >= row or cur_y >= col:
                continue
            if visit[cur_x][cur_y] or not maps[cur_x][cur_y]:
                continue
            visit[cur_x][cur_y] = True
            q.append([cur_x, cur_y, cnt + 1])
    return answer