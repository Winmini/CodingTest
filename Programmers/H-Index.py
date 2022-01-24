def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx, ct in enumerate(citations):
        if idx + 1 <= ct:
            answer = idx + 1
    return answer