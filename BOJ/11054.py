import sys


a = int(input())
seq = [0] + [int(i) for i in sys.stdin.readline().split()] + [0]
bi = [[0] * 2 for i in range(a + 1)]
bi.append([0, 0])

if a == 1:
    print(1)
else:
    bi[1][1] = 1  # 1은 증가
    for i in range(2, a + 1): # 앞에서부터 증가
        tmp_plus = []
        for idx, j in enumerate(seq[1:i]):
            if j < seq[i]:
                tmp_plus.append(bi[idx + 1][1])
        if not tmp_plus:
            bi[i][1] = 1
        else:
            bi[i][1] = max(tmp_plus) + 1
    seq = seq[::-1]  # 뒤집고
    bi = bi[::-1]
    bi[1][0] = 1
    for i in range(2, a + 1):
        tmp_minus = []
        for idx, j in enumerate(seq[1:i]):
            if j < seq[i]:
                tmp_minus.append(bi[idx + 1][0])
        if not tmp_minus:
            bi[i][0] = 1
        else:
            bi[i][0] = max(tmp_minus) + 1
    bi = bi[::-1]
    answer = [x[0] + x[1] for x in bi[1:a+1]]
    print(max(answer) - 1)