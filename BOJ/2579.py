a = int(input())
score = [0]

for i in range(a):
    score.append(int(input()))

if a == 1:
    print(score[1])
elif a == 2:
    print(score[1] + score[2])
else:
    x = [[0 for i in range(a+1)] for j in range(a+1)]
    x[1][0] = score[1]
    x[2][1] = score[1] + score[2]
    x[2][0] = score[2]
    for i in range(3, a + 1):
        x[i][0] = max(x[i-2][0], x[i-2][1]) + score[i]
        x[i][1] = x[i-1][0] + score[i]
    print(max(x[a]))