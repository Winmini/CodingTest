# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    chk = 0
    while progresses:
        n_progresses = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[0] >= 100:
                chk = 1
        if chk:
            for i in progresses:
                if i >= 100:
                    n_progresses +=1
                else:
                    break
            progresses = progresses[n_progresses:]
            speeds = speeds[n_progresses:]
            answer.append(n_progresses)
            chk = 0
    return answer