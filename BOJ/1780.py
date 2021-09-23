import sys

test_size = int(input())

board = []
for i in range(test_size):
    board.append([int(i) for i in sys.stdin.readline().split()])
minus = []
plus = []
zero = []


def q_tree(b):
    tmp_p = 1
    tmp_m = 1
    tmp_z = 1
    for s in b:
        for j in s:
            if j != 1:
                tmp_p = 0
            if j != -1:
                tmp_m = 0
            if j != 0:
                tmp_z = 0
        if tmp_p == tmp_m == tmp_z == 0:
            break
    if tmp_z:
        zero.append(1)
        return
    elif tmp_p:
        plus.append(1)
        return
    elif tmp_m:
        minus.append(1)
        return
    size = len(b)//3
    for j in range(3):
        t1 = []
        t2 = []
        t3 = []
        for k in b[j*size:(j+1)*size]:
            t1.append(k[:size])
            t2.append(k[size:2*size])
            t3.append(k[2*size:])
        q_tree(t1)
        q_tree(t2)
        q_tree(t3)


q_tree(board)
print(len(minus))
print(len(zero))
print(len(plus))