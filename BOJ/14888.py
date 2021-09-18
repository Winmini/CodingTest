import sys


num = int(input())
a = [int(i) for i in sys.stdin.readline().split()]
op = [int(i) for i in sys.stdin.readline().split()]
data = []
is_used = [0] * 4
# 1234 1243


def my_op(cnt, pr):
    if cnt == num:
        data.append(pr)
        return
    else:
        if is_used[0] < op[0]:
            is_used[0] += 1
            my_op(cnt+1, pr + a[cnt])
            is_used[0] -= 1

        if is_used[1] < op[1]:
            is_used[1] += 1
            my_op(cnt+1, pr - a[cnt])
            is_used[1] -= 1

        if is_used[2] < op[2]:
            is_used[2] += 1
            my_op(cnt+1, pr * a[cnt])
            is_used[2] -= 1

        if is_used[3] < op[3]:
            is_used[3] += 1
            if pr * a[cnt] < 0:
                my_op(cnt + 1, -(pr // -a[cnt]))
            else:
                my_op(cnt+1, pr // a[cnt])
            is_used[3] -= 1


my_op(1, a[0])
print(max(data))
print(min(data))