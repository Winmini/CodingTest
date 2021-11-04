T = int(input())
for _ in range(T):
    K = int(input())
    n = 1
    tri = []
    while n*(n+1) // 2 < K:
        tri.append(n*(n+1)//2)
        n += 1
    answer = 0
    for i in tri: # 재귀를 이용하면 훨씬 단축이 가능하지만, 3중포문도 해결이 가능하다.
        for j in tri:
            for k in tri:
                if i + j + k == K:
                    answer = 1
    print(answer)