import sys


def count_leaf_with_recursive(now):
    global answer
    if not graph[now]:
        answer += 1
        return
    for i in graph[now]:
        count_leaf_with_recursive(i)


N = int(input())
graph = [[] for _ in range(N)]
node_info = [int(i) for i in sys.stdin.readline().split()]
visited = [False] * N
erase_node = int(input())
p = dict()
root = []
answer = 0
for i, parent in enumerate(node_info):
    if parent == -1:
        root.append(i)
    else:
        graph[parent].append(i)
        p[i] = parent
if erase_node in root:
    root.remove(erase_node)
else:
    graph[p[erase_node]].remove(erase_node)
for i in root:
    count_leaf_with_recursive(i)
print(answer)