
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    first = [i%5 + 1 for i in range(10000)]
    second = [2,1,2,3,2,4,2,5]*1250
    third = [3,3,1,1,2,2,4,4,5,5]*1000
    f_sol = 0
    s_sol = 0
    t_sol = 0
    for i in range(len(answers)):
        if first[i] == answers[i]:
            f_sol += 1
        if second[i] == answers[i]:
            s_sol += 1
        if third[i] == answers[i]:
            t_sol += 1
    answer = sorted([[f_sol, 1], [s_sol, 2], [t_sol, 3]], reverse=True)
    if answer[0][0] > answer[1][0]:
        return [answer[0][1]]
    elif answer[1][0] > answer[2][0]:
        return sorted([answer[0][1], answer[1][1]])
    else:
        return sorted([answer[0][1], answer[1][1], answer[2][1]])