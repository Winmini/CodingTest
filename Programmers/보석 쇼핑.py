# https://programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    solution = len(set(gems))
    gems_size = len(gems)
    start = 0
    end = 0
    answer = [0, 100000]
    gem = {gems[0]:1}
    gem_sum = 1
    if solution == 1:
        return [1, 1]
    while True:
        try:
            if end != gems_size:
                end += 1
                for i in range(end, gems_size):
                    if gems[i] in gem:
                        gem[gems[i]] += 1
                    else:
                        gem[gems[i]] = 1
                        if len(gem) == solution:
                            end = i
                            break
            
            for i in range(start,gems_size):
                if gem[gems[i]] == 1:
                    del gem[gems[i]]
                    if len(gem) == solution - 1:
                        start = i + 1
                        break
                else:
                    gem[gems[i]] -=1
        except:
            return answer
        else:
            if (answer[1]-answer[0]) > (end + 1 - start):
                answer = [start, end+1]
                if end - start - 1 == solution:
                    return answer