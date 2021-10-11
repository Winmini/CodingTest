import sys
from itertools import combinations

L, C = [int(i) for i in sys.stdin.readline().split()]
secret = sorted(sys.stdin.readline().split())
answer = list(combinations(secret, L))
for a in answer:
    vowels = a.count('a') + a.count('e') + a.count('i') + a.count('o') + a.count('u')
    consonants = len(a) - vowels
    if vowels >= 1 and consonants >= 2:
        print(''.join(a))