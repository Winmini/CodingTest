T = int(input())

for test_case in range(1, T+1):
    answer = 0
    baby_gin = [int(i) for i in input().split()]
    player_1 = [0] * 10
    player_2 = [0] * 10
    answer = 0
    for i, n in enumerate(baby_gin):
        if i % 2:
            player_2[n] += 1
        else:
            player_1[n] += 1
        for j in range(8):
            if player_1[j] > 0 and player_1[j+1] > 0 and player_1[j+2] > 0:
                answer = 1
                break
            if player_2[j] > 0 and player_2[j+1] > 0 and player_2[j+2] > 0:
                answer = 2
                break
        if player_1[n] == 3:
            answer = 1
            break
        if player_2[n] == 3:
            answer = 2
            break
        if answer:
            break

    print('#' + str(test_case) + ' ' + str(answer))