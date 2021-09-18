a = int(input())
b = []
board1 = [0] * a
board2 = [0] * a * a
board3 = [0] * a * a


def queen(n): # n번쨰 퀸
    if n == a:
        b.append(1)
        return
    else:
        for i in range(a): # i열번째
            if not board1[i] and not board2[n+i] and not board3[a-n+i+1]:
                board1[i] = 1
                board2[n+i] = 1
                board3[a-n+i+1] = 1
                queen(n+1)
                board1[i] = 0
                board2[n+i] = 0
                board3[a-n+i+1] = 0


queen(0)
print(len(b))