from collections import deque


def solve(x):
    if x == "":
        return ""
    u = [0, 0]
    l_ans = ""
    r_ans = ""
    tmp = ""
    for idx, i in enumerate(x):
        tmp += i
        if i == "(":
            u[0] += 1
        else:
            u[1] += 1
        if u[0] == u[1]:
            l_ans = tmp
            r_ans = x[idx + 1:]
            break
    if checkRight(l_ans):
        return l_ans + solve(r_ans)
    else:
        new_u = ""
        for i in l_ans[1:-1]:
            if i == "(":
                new_u += ")"
            else:
                new_u += "("
        return "(" + solve(r_ans) + ")" + new_u

def checkRight(x):
    ck = deque([])
    for i in x:
        if i == "(":
            ck.append(i)
        elif i == ")" and ck:
            ck.pop()
        else:
            return False
    return True


def solution(p):      
    answer = solve(p)
    return answer