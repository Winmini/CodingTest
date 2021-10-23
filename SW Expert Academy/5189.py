from itertools import permutations
INF = int(1e9)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append([int(i) for i in input().split()])
    answer = INF
    for per in permutations([i for i in range(N)]):
        t_answer = 0
        for i in range(N - 1):
            t_answer += board[per[i]][per[i+1]]
        answer = min(answer, t_answer + board[per[-1]][per[0]])
    print("#" + str(test_case) + " " + str(answer))
