# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    K={}
    for i in clothes:
        if i[1] in K:
            K[i[1]] +=1
        else:
            K[i[1]] = 1
    answer = 1
    for i in K:
        answer *= (K[i]+1) 
    return answer-1