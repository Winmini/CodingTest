def solution(distance, rocks, n):
    rocks.sort()
    start = 0 
    end = distance
    answer = 0

    while start <= end:
        mid = (start + end) >> 1
        cnt = 0
        standard = 0
        for rock in rocks:
            if rock - standard < mid:
                cnt += 1
            else:
                standard = rock
            if cnt > n:
                break
        if cnt > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer