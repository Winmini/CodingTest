# https://programmers.co.kr/learn/courses/30/lessons/42587#


def solution(priorities, location):
    location = [priorities[location],location]
    tmp = [[priorities[i],i] for i in range(len(priorities))]
    priorities = tmp
    answer = []
    while True:
        pr = max(priorities)
        if pr == [0]:
            break
        for i in range(len(priorities)):
            if pr[0] == priorities[0][0]:
                answer.append(priorities[0])
                priorities[0] = [0]
                break
            else:
                priorities.append(priorities[0])
                priorities.pop(0)
    for i in range(len(answer)):
        if location == answer[i]:
            return i+1