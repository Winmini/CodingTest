import sys


a = int(input())
conf = []
for i in range(a):
    conf.append([int(i) for i in sys.stdin.readline().split()])
conf = sorted(conf, key=lambda x: (x[1], x[0]))

answer = 1
end_time = conf[0][1]
start_time = 0
for idx in range(1, len(conf)):
    if end_time <= conf[idx][0]:
        answer += 1
        end_time = conf[idx][1]
print(answer)