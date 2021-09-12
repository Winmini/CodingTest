# 문제: https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = 7
    n_zero = [0 for i in lottos if not i]
    n_lottos = [i for i in lottos if i]
    for i in win_nums:
        if i in n_lottos:
            answer -= 1
    a = answer - len(n_zero)
    b = answer
    if a == 7:
        a = 6
    if b == 7:
        b = 6
    return [a, b]