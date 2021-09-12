# https://programmers.co.kr/learn/courses/30/lessons/62048

def solution(w,h):
    answer = h + w
    for i in range(1,w+1):
        if not h*i%w:
            return h*w-answer+w/i