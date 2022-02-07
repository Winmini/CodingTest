import sys
sys.setrecursionlimit(10**6)

parent = {}

def find(target):
    if not target in parent:
        parent[target] = target
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

def solution(k, room_number):
    
    answer = [0] * len(room_number)

    for idx, i in enumerate(room_number):
        if not i in parent:
            answer[idx] = i
            if i + 1 in parent:
                union(i, i+1)
            else:
                parent[i] = i + 1
                parent[i+1] = i + 1
        elif i in parent and i == parent[i]:
            answer[idx] = parent[i]
            if i + 1 in parent:
                union(i, i+1)
            else:
                parent[i] = i + 1
                parent[i+1] = i+1
        else:
            answer[idx] = find(i)
            if answer[idx] + 1 in parent:
                union(answer[idx], answer[idx]+1)
            else:
                parent[answer[idx]] = answer[idx] + 1
                parent[answer[idx] + 1] = answer[idx] + 1

    return answer