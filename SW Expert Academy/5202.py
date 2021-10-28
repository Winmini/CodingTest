T = int(input())

for test_case in range(1, T+1):
    answer = 0
    N = int(input())
    apply_list = []
    for _ in range(N):
        apply_list.append([int(i) for i in input().split()])
    apply_list.sort(reverse=True, key=lambda x: x[1])
    end_time = 0
    while apply_list:
        st, ed = apply_list.pop()
        if st >= end_time:
            answer += 1
            end_time = ed
    print('#' + str(test_case) + ' ' + str(answer))s