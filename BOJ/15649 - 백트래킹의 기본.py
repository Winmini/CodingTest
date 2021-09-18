import sys


def back(k):
    if k == a[1]:
        for i in arr:
            print(i, end=' ')
        print()
        return
    else:
        for idx, i in enumerate(chk):
            if not i:
                arr[k] = idx + 1
                chk[idx] = 1
                back(k + 1)
                chk[idx] = 0


a = [int(i) for i in sys.stdin.readline().split()]
chk = [0] * a[0]
arr = [0] * a[1]
back(0)
