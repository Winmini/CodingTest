def solution(numbers, target):
    answer = 0
    data = [-numbers[0], numbers[0]]
    for i in numbers[1:]:
        tmp = []
        for j in data:
            tmp.append(j + i)
            tmp.append(j - i)
        data = tmp
    for i in data:
        if i == target:
            answer += 1
    return answer
    
    
    
'''
배울만한 코드
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
'''