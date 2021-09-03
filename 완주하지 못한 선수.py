# 1 zip을 이용한 풀이
def solution(participant, completion):
    for x, y in zip(sorted(participant), sorted(completion)):
        if x!=y:
            return x
    return sorted(participant)[-1]


# 2 Counter객체를 이용한 풀이
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]