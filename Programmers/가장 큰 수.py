https://programmers.co.kr/learn/courses/30/lessons/42746#

def solution(numbers):
    numbers = [str(i) for i in numbers]
    answer = ''
    tmp = []
    for i in numbers:
        t = i
        while len(i) < 4:
            i += i
        tmp.append([i,t])
    numbers = sorted(tmp, key=lambda x: x[0], reverse=True)
    for i in numbers:
        answer += i[1]
    if not int(answer):
        return "0"
    return answer