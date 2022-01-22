score = 0
answer = [0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0]
def solution(n, info):
    result = [0,0,0,0,0,0,0,0,0,0,0]
    global answer
    def dfs(i, n):
        global answer
        global score
        if i == 11:
            a = 0
            l = 0
            for i in range(11):
                if info[i] < result[i]:
                    l += (10 - i)
                elif info[i] > result[i]:
                    a += (10 - i)
            if score < l - a:
                score = l - a
                answer = result[:]
            elif score == l - a and score != 0:
                if sum([i*answer[i] for i in range(11)]) < sum([i*result[i] for i in range(11)]):
                    answer = result[:]
            return
        if info[i] < n:
            result[i] += info[i] + 1
            dfs(i + 1, n - info[i] - 1)
            result[i] -= info[i] + 1
            dfs(i + 1, n)
        else:
            dfs(i + 1, n)
    dfs(0, n)
    if sum(answer) == 0:
        answer = [-1]
    elif sum(answer) < n:
        answer[-1] += (n-sum(answer))
    return answer