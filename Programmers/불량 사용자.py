import re


def solution(user_id, banned_id):
    com = []
    answer = []
    r = []
    
    def bt(n):
        if n == len(answer):
            com.sort()
            s = '_'.join(com)
            if s not in r:
                r.append(s)
            return
        else:
            for i in answer[n]:
                if i in com:
                    continue
                com.append(i)
                bt(n+1)   
                com.remove(i)
    
    user_id = ' '.join(user_id)
    for b_id in banned_id:
        p = re.compile(r'\b' + b_id.replace('*', '\w') + r'\b')
        answer.append(p.findall(user_id))
    bt(0)
    return len(r)