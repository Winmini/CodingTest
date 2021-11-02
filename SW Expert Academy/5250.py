import heapq


INF = int(1e9)
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


T = int(input())
for test_case in range(1, T + 1):
    v = int(input())
    visit = [[False] * v for _ in range(v)]
    dist = [[INF] * v for _ in range(v)]
    board = []
    for _ in range(v):
        board.append([int(i) for i in input().split()])
    q = []
    heapq.heappush(q, (0, 0, 0))
    dist[0][0] = 0
    while q:
        dis, now_x, now_y = heapq.heappop(q)
        if visit[now_x][now_y]:
            continue
        visit[now_x][now_y] = True
        for i in range(4):
            cur_x = now_x + dir_x[i]
            cur_y = now_y + dir_y[i]
            if 0 <= cur_x < v and 0 <= cur_y < v:
                dist_update = dist[now_x][now_y] + 1
                if board[cur_x][cur_y] > board[now_x][now_y]:
                    dist_update += board[cur_x][cur_y] - board[now_x][now_y]
                if dist[cur_x][cur_y] < dist_update:
                    continue
                dist[cur_x][cur_y] = dist_update
                heapq.heappush(q, (dist_update, cur_x, cur_y))
    print('#{} {}'.format(test_case, dist[v-1][v-1]))