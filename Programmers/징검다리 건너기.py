def solution(stones, k):
    start = 0
    end = 200000000
    answer = 0
    while start <= end:
        mid = (start + end ) >> 1
        tmp = 0
        t_answer = 0
        for i in stones:
            if i - mid < 0:
                tmp += 1
            else:
                tmp = 0
            t_answer = max(t_answer, tmp)
        if t_answer >= k:
            end = mid-1
        else:
            answer = mid
            start = mid+1
    return answer