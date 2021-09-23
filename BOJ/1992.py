test_size = int(input())

board = []
for i in range(test_size):
    board.append(input())
answer = []


def q_tree(b):
    tmp = 0
    for k in b:
        tmp += int(k)
    if tmp == int('1'*len(b))*len(b):
        answer.append('1')
    elif tmp == 0:
        answer.append('0')
    else:
        tmp1 = []
        tmp2 = []
        for idx in b[:len(b)//2]:
            tmp1.append(idx[:len(b)//2])
            tmp2.append(idx[len(b)//2:])
        answer.append('(')
        q_tree(tmp1)
        q_tree(tmp2)
        tmp1 = []
        tmp2 = []
        for idx in b[len(b)//2:]:
            tmp1.append(idx[:len(b)//2])
            tmp2.append(idx[len(b)//2:])
        q_tree(tmp1)
        q_tree(tmp2)
        answer.append(')')


q_tree(board)
x = ''
for i in answer:
    x += i
print(x)s