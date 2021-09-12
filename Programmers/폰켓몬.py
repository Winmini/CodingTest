# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    if 2*len(set(nums)) < len(nums):
        return len(set(nums))
    else:
        return len(nums)/2