def solution(n, times):
    start = 1
    end = int(1e22)
    while start <= end:
        mean = (start + end) >> 1
        exam_time = 0
        for i in times:
            exam_time += mean//i
        if exam_time >= n:
            end = mean - 1
        elif exam_time < n:
            start = mean + 1
    return start