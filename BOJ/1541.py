a = input()
min_pr = ''
first = 1
for i in a:
    if first and i == '-':
        min_pr += '-('
        first = 0
    elif i == '-':
        min_pr += ')-('
    else:
        min_pr += i
if not first:
    min_pr += ')'
answer = ''
chk = 1
for i in min_pr:
    if i == '+' or i == '-' or i == '(':
        answer += i
        chk = 1
    else:
        if chk != 1 or i != '0':
            answer += i
            chk = 0
print(eval(answer))