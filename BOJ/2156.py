a = int(input())

wine = [0]
for i in range(1, a + 1):
    wine.append(int(input()))
eat = [[0] * 2 for i in range(10001)]
eat[1][0] = wine[1]
if a == 1:
    print(eat[1][0])
else:
    eat[2][0] = wine[2]
    eat[2][1] = wine[1] + wine[2]
    if a == 2:
        print(eat[2][1])
    else:
        for i in range(3, a+1):
            eat[i][0] = max(eat[i-2][0], eat[i-2][1], eat[i-3][0], eat[i-3][1]) + wine[i]
            eat[i][1] = eat[i-1][0] + wine[i]
        print(max(eat[a][0], eat[a][1], eat[a-1][0], eat[a-1][1]))