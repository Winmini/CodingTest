INF = int(1e9)


def bus(now_battery, now_stop, end_stop, trade_num):
    global answer
    if now_battery >= end_stop - now_stop:
        answer = min(answer, trade_num)
        return
    if trade_num >= answer:
        return 
    else:
        if now_battery == 0:
            bus(battery[now_stop] - 1, now_stop+1, end_stop, trade_num + 1)
        elif now_battery < battery[now_stop]:
            bus(battery[now_stop] - 1, now_stop+1, end_stop, trade_num + 1)
            bus(now_battery - 1, now_stop+1, end_stop, trade_num)
        else:
            bus(now_battery - 1, now_stop + 1, end_stop, trade_num)


T = int(input())
for test_case in range(1, T+1):
    answer = INF
    battery = [int(i) for i in input().split()]
    bus(battery[1]-1, 2, battery[0], 0)
    print('#' + str(test_case) + ' ' + str(answer))