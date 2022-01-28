def solution(play_time, adv_time, logs):
    end_time = int(play_time[:2]) * 3600 + int(play_time[3:5]) * 60 + int(play_time[6:])
    time = [0] * (end_time + 1)
    for log in logs:
        time[int(log[:2]) * 3600 + int(log[3:5]) * 60 + int(log[6:8])] += 1
        time[int(log[9:11]) * 3600 + int(log[12:14]) * 60 + int(log[15:])] -= 1

    sumTime = [0] * (end_time + 2)
    for t in range(len(time)):
        sumTime[t + 1] += sumTime[t] + time[t]
    subsum = [0] * (end_time + 3)
    for t in range(len(sumTime)):
        subsum[t + 1] += sumTime[t] + subsum[t]
        
    adver_time = int(adv_time[:2]) * 3600 + int(adv_time[3:5]) * 60 + int(adv_time[6:]) - 1
    answer = 0
    result = 0
    for i in range(len(sumTime) - adver_time):
        if answer < subsum[adver_time + i + 1] - subsum[i]:
            result = i - 1
            answer = subsum[adver_time + i + 1] - subsum[i]
    if result < 0:
        result = 0 
    hour = format(result // 3600, '02')
    result %= 3600
    minute = format(result // 60, '02')
    result %= 60
    second = format(result, '02')
    timeStr = hour  + ":" + minute + ":" + second
    return timeStr