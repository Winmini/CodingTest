import sys

test_size = int(input())

paper = []
for i in range(test_size):
    paper.append([int(i) for i in sys.stdin.readline().split()])

blue = []
white = []


def cut_the_paper(p):
    tmp = 0
    for k in p:
        tmp += sum(k)
    if tmp == pow(len(p), 2):
        blue.append(1)
        return
    elif tmp == 0:
        white.append(1)
        return
    else:
        tmp1 = []
        tmp2 = []
        for idx in p[:len(p)//2]:
            tmp1.append(idx[:len(p)//2])
            tmp2.append(idx[len(p)//2:])
        cut_the_paper(tmp1)
        cut_the_paper(tmp2)
        tmp1 = []
        tmp2 = []
        for idx in p[len(p)//2:]:
            tmp1.append(idx[:len(p)//2])
            tmp2.append(idx[len(p)//2:])
        cut_the_paper(tmp1)
        cut_the_paper(tmp2)


cut_the_paper(paper)
print(len(white))
print(len(blue))