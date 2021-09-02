def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        for b in board:
            if b[move - 1]:
                bucket.append(b[move - 1])
                b[move - 1] = 0
                break
    chk = 1
    tmp = 0
    while chk:
        chk = 0
        for doll in range(len(bucket)):
            if bucket[doll] == tmp:
                del bucket[doll]
                del bucket[doll - 1]
                answer += 2
                tmp = 0
                chk = 1
                break
            tmp = bucket[doll]
        
    return answer