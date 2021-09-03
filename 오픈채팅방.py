# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    answer2 = []
    id = {}
    for rcd in record:
        tmp = rcd.split()
        if tmp[0] == 'Enter':
            id[tmp[1]] = tmp[2]
            answer.append(tmp[1] + '님이 들어왔습니다.')
        if tmp[0] == 'Leave':
            answer.append(tmp[1] + '님이 나갔습니다.')
        if tmp[0] == 'Change':
            id[tmp[1]] = tmp[2]


    for tmp in answer:
        answer2.append(tmp.replace(tmp.split('님')[0], id[tmp.split('님')[0]]))
    
    return answer2