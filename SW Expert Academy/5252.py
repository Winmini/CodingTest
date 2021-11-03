T = int(input())
for test_case in range(1, T + 1):
    first, second = [int(i) for i in input().split()]
    memo_1, memo_2 = [], []
    for _ in range(first):
        memo_1.append(input())
    for _ in range(second):
        memo_2.append(input())
    answer = 0
    for word in memo_1:
        if word in memo_2:
            answer += 1
    
    print('#{} {}'.format(test_case, answer))