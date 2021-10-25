from itertools import product
import sys


N = int(input())
A = [int(i) for i in sys.stdin.readline().split()]
num_op = [int(i) for i in sys.stdin.readline().split()]
d_op = list(product(['+', '-', '*', '/'], repeat=N-1))
ops = []
for op in d_op:
    if op.count('+') <= num_op[0] and op.count('-') <= num_op[1] and op.count('*') <= num_op[2] and op.count('/') <= num_op[3]:
        ops.append(op)
answer = []
for op in ops:
    t = A[0]
    for i, o in enumerate(op):
        if o == '+':
            t += A[i + 1]
        if o == '-':
            t -= A[i + 1]
        if o == '*':
            t *= A[i + 1]
        if o == '/':
            if t < 0 and A[i + 1] > 0:
                t = -((-t) // A[i+1])
            else:
                t //= A[i + 1]
    answer.append(t)
print(max(answer))
print(min(answer))