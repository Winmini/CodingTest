# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people = sorted(people)
    answer = 0
    start = 0
    end = len(people) - 1
    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    return answer