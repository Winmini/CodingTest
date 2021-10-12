a = int(input())
answer = ['2', '3', '5', '7']
for _ in range(a - 1):
    tmp = []
    for i in answer:
        for j in ['1', '3', '5', '7', '9']:
            chk = 1
            for k in range(2, int(int(i+j)**0.5 + 1)):
                if not int(i + j) % k:
                    chk = 0
                    break
            if chk:
                tmp.append(i+j)
    answer = tmp
for i in answer:
    print(i)