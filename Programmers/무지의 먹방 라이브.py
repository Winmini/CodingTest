def solution(food_times, k):
    answer = 0
    start = 0
    end = max(food_times)
    size = len(food_times)
    cnt = 0
    newFood_times = []
    error = k
    while start <= end:
        mid = (start + end) >> 1
        error = k
        newFood_times = []
        cnt = 0
        for i in food_times:
            if i <= mid:
                error -= i
                newFood_times.append(0)
            else:
                error -= mid
                cnt += 1
                newFood_times.append(i - mid)
            if error < 0:
                break
        if 0 <= error < cnt:
            break
        elif error < 0:
            end = mid - 1
        else:
            start = mid + 1

    for i in newFood_times:
        if i != 0 and error == 0:
            answer += 1
            break
        elif i != 0 and error > 0:
            answer += 1
            error -= 1
        elif i == 0:
            answer += 1
    if sum(newFood_times):
        return answer
    return -1