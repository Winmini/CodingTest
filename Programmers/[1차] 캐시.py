from collections import deque
    


def solution(cacheSize, cities):
    cities = list(map(str.upper, cities))
    cache = deque([0] * cacheSize)
    answer = 0
    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            cache.popleft()
            answer += 5
    return answer