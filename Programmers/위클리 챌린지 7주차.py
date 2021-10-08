def solution(enter, leave):
    answer = [0] * len(enter)
    stack = []
    leave = leave[::-1]
    for i in enter:
        stack.append(i)
        if len(stack) >= 2:
            for j in range(len(stack)-1):
                answer[stack[j]-1] += 1
                answer[stack[-1]-1] += 1
        while leave[-1] in stack:
            stack.pop(stack.index(leave[-1]))
            leave.pop()
            if not leave:
                break
    return answer