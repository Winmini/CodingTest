import bisect


def solution(n, t, m, timetable):
    timetable = [int(i[:2])*60 + int(i[3:]) for i in sorted(timetable)]
    start = 0
    end = 1439
    while start <= end:
        mean = (start + end) >> 1
        timetable.insert(bisect.bisect_right(timetable, mean), float(mean) + 0.5)
        can_ride = 0
        now = 0
        for i in range(n):
            for j in range(m):
                if timetable[now] == float(mean) + 0.5 and mean <= 540 + i*t:
                    can_ride = 1
                    break
                if timetable[now] <= 540 + i*t:
                    now += 1
        if can_ride == 1:
            start = mean + 1
        else:
            end = mean - 1
        timetable.remove(float(mean) + 0.5)
    hour = str(end//60)
    if len(hour) == 1:
        hour = '0' + hour
    minute = str(end%60)
    if len(minute) == 1:
        minute = '0' + minute
    answer = hour + ":" + minute
    return answer