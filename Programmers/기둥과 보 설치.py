def solution(n, build_frame):
    pillar = [[False] * (n+10) for _ in range(n+1)]
    bar = [[False] * (n+10) for _ in range(n+1)]
    
    for y, x, typ, state in build_frame:
        y += 5
        
        if typ and state:
            if x == 0:
                continue
            if pillar[x-1][y] or pillar[x-1][y+1] or (bar[x][y-1] and bar[x][y+1]):
                bar[x][y] = True
                
        elif typ and not state: # 보 삭제
            if x == 0:
                continue
            if pillar[x][y]:
                if not bar[x][y-1] and not pillar[x-1][y]:
                    continue
            if pillar[x][y+1]:
                if not bar[x][y+1] and not pillar[x-1][y+1]:
                    continue
            if bar[x][y-1]:
                if not pillar[x-1][y] and not pillar[x-1][y-1]:
                    continue
            if bar[x][y+1]:
                if not pillar[x-1][y+1] and not pillar[x-1][y+2]:
                    continue
            bar[x][y] = False
        
        elif not typ and state:
            if x == 0:
                pillar[x][y] = True
            elif bar[x][y] or bar[x][y-1] or pillar[x-1][y]:
                pillar[x][y] = True
        
        else:
            if pillar[x+1][y]:
                if not bar[x+1][y] and not bar[x+1][y-1]:
                    continue
            if bar[x+1][y]:
                if not pillar[x][y+1] and (not bar[x+1][y-1] or not bar[x+1][y+1]):
                    continue
            if bar[x+1][y-1]:
                if not pillar[x][y-1] and (not bar[x+1][y] or not bar[x+1][y-2]):
                    continue
            pillar[x][y] = False
        
    result = []
    for i in range(n+1):
        for j in range(n+10):
            if bar[i][j]:
                result.append([j-5,i,1])
            if pillar[i][j]:
                result.append([j-5,i,0])

    return sorted(result)