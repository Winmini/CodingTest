import datetime


def solution(lines):
    answer = 0
    times = []
    for l in lines:
        _, date_time_str, time = l.split()
        ed_t = datetime.datetime.strptime(date_time_str, '%H:%M:%S.%f')
        st_t = ed_t - datetime.timedelta(seconds=float(time[:-1]) + 0.999)
        times.append([st_t, 'st'])
        times.append([ed_t, 'ed']) 
    work = 0
    for time, state in sorted(times):
        if state == 'st':
            work += 1
            answer = max(answer, work)
        elif state == 'ed':
            work -= 1
    return answer
