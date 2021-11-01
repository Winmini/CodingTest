def make_set(x):
    p[x] = x


def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union_set(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1


T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    p = [i for i in range(v + 1)]  # make_set
    rank = [0] * (v + 1)
    edge = []
    for _ in range(e):
        edge.append([int(i) for i in input().split()])
    edge.sort(key=lambda x: -x[2])
    mst = []
    min_cost = 0
    while len(mst) < v:
        a, b, w = edge.pop()
        if find_set(a) != find_set(b):
            union_set(a, b)
            mst.append((a, b))
            min_cost += w
    print('#{} {}'.format(test_case, min_cost))