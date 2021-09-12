# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq as hq

def solution(operations):
    heap = []
    for i in operations:
        if i[0] == 'I':
            hq.heappush(heap,int(i[2:]))
        elif i[2] == '-':
            if len(heap):
                hq.heappop(heap)
        else:
            if len(heap):
                heap.remove(max(heap))
    if len(heap):
        return [max(heap), min(heap)]
    else:
        return [0,0]