a = int(input())
x = [i for i in range(1, a + 1)[::-1]]  # 이 숫자로 num을 만들자.
num = []  # 만들어야 하는 숫자

stack = []
answer = []
for i in range(a):
    num.append(int(input()))
i = 0

while x:  # stack과 수열이 모두 빌때까지 진행
    if x:
        stack.append(x[-1])
        x.pop()
        answer.append('+')
    while stack[-1] == num[i]:
        stack.pop()
        answer.append('-')
        i += 1
        if not stack:
            break

if stack:
    print('NO')
else:
    for i in answer:
        print(i)