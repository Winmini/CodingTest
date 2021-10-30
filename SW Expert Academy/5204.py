from collections import deque


def merge_sort(l):
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(deque(left), deque(right))


def merge(left, right):
    global answer
    result = []
    if left[-1] > right[-1]:
        answer += 1
    while len(left) > 0 and len(right) > 0:
        if left[0] >= right[0]:
            result.append(right.popleft())
        else:
            result.append(left.popleft())
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result


T = int(input())
for test_case in range(1, T+1):
    answer = 0
    N = int(input())
    ai = [int(i) for i in input().split()]
    sorted_list = merge_sort(ai)
    print('#' + str(test_case) + ' ' + str(sorted_list[len(sorted_list)//2]) + ' ' + str(answer))