# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    time = 1
    t_list = []
    t_weight = 0
    # while True:
    while True:
        time += 1
        if truck_weights:
            if weight >= t_weight + truck_weights[0]:
                t_list.append([bridge_length, truck_weights[0]])
                t_weight += truck_weights[0]
                truck_weights.pop(0)
        for i in range(len(t_list)):
            t_list[i][0] -=1
        if not t_list[0][0]:
            t_weight -= t_list[0][1]
            t_list.pop(0)
        if not truck_weights:
            if not t_list:
                break
    return time
