def kmp_preprocess(p, kmp_next):
    M = len(p)
    i = 0
    j = -1
    while i < M:
        kmp_next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = kmp_next[j]
        i += 1
        j += 1


def kmp_search(t, p, kmp_next):
    N = len(t)
    M = len(p)
    i = 0
    j = 0
    while i < N:
        while i >= 0 and t[i] != p[j]:
            j = kmp_next[j]
        i += 1
        j += 1
        if j == M:
            return i-j
    return -1