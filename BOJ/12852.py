a = int(input())
x = [[0] * 2 for _ in range(a+1)]
# 앞은 횟수, 뒤는 어디서 왔나
if a == 1:
    print(0)
    print(1)
else:
    x[1][0] = 0
    x[1][1] = 1
    x[2][0] = 1
    x[2][1] = 1
    for i in range(2, a + 1):
        x[i][0] = x[i-1][0] + 1
        x[i][1] = i-1
        if i % 3 == 0 and i % 2:
            if x[i//3][0] + 1 < x[i][0]:
                x[i][0] = x[i//3][0] + 1
                x[i][1] = i//3
        elif i % 2 == 0 and i % 3:
            if x[i//2][0] + 1 < x[i][0]:
                x[i][0] = x[i//2][0] + 1
                x[i][1] = i//2
        elif i % 2 == 0 and i % 3 == 0:
            tmp = sorted([[x[i//2][0] + 1, i//2], [x[i//3][0] + 1, i//3], [x[i][0], i-1]], key=lambda x: x[0])
            x[i][0] = tmp[0][0]
            x[i][1] = tmp[0][1]
    print(x[a][0])
    print(a, end=' ')
    answer = a
    while answer != 1:
        answer = x[answer][1]
        print(answer, end=' ')