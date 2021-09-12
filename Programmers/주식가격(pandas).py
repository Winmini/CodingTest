# https://programmers.co.kr/learn/courses/30/lessons/42584#

def solution(prices):
    size = len(prices)
    answer = [0 for i in prices]
    tmp = []
    for i in range(size):
        tmp.append([i,prices[i]])
        for j in range(len(tmp)):
            if prices[i] < tmp[j][1]:
                answer[tmp[j][0]] = (i-tmp[j][0])
                tmp[j]=[0]
        for j in range(len(tmp)):
            try:
                tmp.remove([0])
            except:
                break
    for i in tmp:
        answer[i[0]] = size - i[0] - 1
    return answer

# pandas 모델, 정확성 통과, 효율성 탈락
# import numpy as np
# import pandas as pd


# def solution(prices):
#     pr = pd.Series(prices)
#     answer = []
#     for i in range(len(prices)):
#         if list(pr[i+1:].loc[pr<pr[i]]):
#             answer.append(list(pr[i+1:].loc[pr<pr[i]].index)[0] - i)
#         else:
#             answer.append(len(prices) - i - 1)
#     return answer