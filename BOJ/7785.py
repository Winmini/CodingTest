import sys


N = int(input())
company = set()
for _ in range(N):
    name, commute = sys.stdin.readline().split()
    if commute == 'enter':
        company.add(name)
    elif commute == 'leave':
        company.remove(name)
for name in sorted(list(company), reverse=True):
    print(name)