T = int(input())

for test_case in range(1, T+1):
    N, M = [int(i) for i in input().split()]
    answer = 0
    weights = [int(i) for i in input().split()]
    truck = [int(i) for i in input().split()]
    weights.sort()
    truck.sort()
    while weights and truck:
        if truck[-1] >= weights[-1]:
            answer += weights[-1]
            weights.pop()
            truck.pop()
        else:
            weights.pop()
    print('#' + str(test_case) + ' ' + str(answer))