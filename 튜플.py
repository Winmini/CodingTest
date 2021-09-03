def solution(s):
    num_data = []
    t = ''
    for i in s[1:-1]:
        if (i!='{') & (i!='}') & (i!=','):
            t += i
        else:
            if t != '':
                num_data.append(t)
            t = ''
    s = num_data
    n_s = [0 for i in set(s)]
    k_s = {i:0 for i in set(s)}
    for i in s:
        k_s[i] += 1
    for i in k_s:
        n_s[len(n_s)-k_s[i]] = int(i)
    return tuple(n_s)