# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        try:
            if scoville[0] < K:
                heapq.heappush(scoville,heapq.heappop(scoville) + 2*heapq.heappop(scoville))
                answer+=1
            else:
                break
        except:
            return -1
    return answer