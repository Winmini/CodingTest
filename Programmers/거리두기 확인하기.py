dx1 = [1,0,-1,0]
dy1 = [0,1,0,-1] # 상하좌우

dx2 = [1,-1,1,-1]
dy2 = [1,1,-1,-1] # 대각선


def checkKeepDistance(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                for dis in range(4):
                    cur_x = i + dx1[dis]
                    cur_y = j + dy1[dis]
                    if cur_x < 0 or cur_x >= 5 or cur_y < 0 or cur_y >= 5:
                        continue
                    if place[cur_x][cur_y] == 'P':
                        return 0
                for dis in range(4):
                    cur_x = i + dx1[dis]*2
                    cur_y = j + dy1[dis]*2
                    if cur_x < 0 or cur_x >= 5 or cur_y < 0 or cur_y >= 5:
                        continue
                    if place[cur_x][cur_y] == 'P' and place[i + dx1[dis]][j + dy1[dis]] != 'X':
                        return 0
                for dis in range(4):
                    cur_x = i + dx2[dis]
                    cur_y = j + dy2[dis]
                    if cur_x < 0 or cur_x >= 5 or cur_y < 0 or cur_y >= 5:
                        continue
                    if place[cur_x][cur_y] == 'P':
                        if place[i + dx2[dis]][j] != 'X' or place[i][j + dy2[dis]] != 'X':
                            return 0
    return 1

def solution(places):
    row = 5
    column = 5
    visited = [[False]*column for j in range(row)]
    result = []
    for place in places:
        result.append(checkKeepDistance(place))
    return result