# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s)
    same = 0
    txt = 
    result = 10000
    cont = 0
    for j in range(1,len(s)+1) # j가 자르는 갯수
        tmp = []
        tmp.extend(s[ii+j] for i in range(0, len(s), j)) 
        for k in tmp
            if txt == k and not cont
                same += (j - 1)
                cont += 1
            elif txt == k and cont = 1
                same += j
                cont += 1
                if cont == 9
                    same -= 1
                if cont == 99
                    same -= 1
            else
                cont = 0
            txt = k
        t_result = len(s) - same
        if t_result  result
            result = t_result
        same = 0
    return result