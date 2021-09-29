x = int(input())
if x == 1:
    print(0)
elif x == 2:
    print(1)
else:
    a = [1, x]
    b = [True] * (a[1] + 1)
    m = int(a[1] ** 0.5)
    for i in range(2, m+1):
        if b[i]:
            for j in range(2*i,a[1]+1,i):
                b[j] = False
    if a[0] == 1:
        a[0] = 2
    seq = []
    for k in [i for i in range(a[0], a[1]+1) if b[i]]:
        seq.append(k)
    start = -1
    end = 1
    answer = 0
    seq_sum = []
    tmp = 0
    for i in seq:
        tmp += i
        seq_sum.append(tmp)

    while end != len(seq):
        tmp = 0
        if start == -1:
            tmp = seq_sum[end]
        else:
            tmp = seq_sum[end] - seq_sum[start]

        if tmp == a[1]:
            answer += 1
            start += 1
            end += 1
        elif tmp < a[1]:
            end += 1
        else:
            start += 1
    print(answer)
