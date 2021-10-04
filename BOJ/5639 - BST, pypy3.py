INF = int(1e9)
import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order(node):
    print(node.data)
    if node.left: pre_order(node.left)
    if node.right: pre_order(node.right)


def in_order(node):
    if node.left: in_order(node.left)
    print(node.data)
    if node.right: in_order(node.right)


def post_order(node):
    if node.left: post_order(node.left)
    if node.right: post_order(node.right)
    print(node.data)


root = Node(int(sys.stdin.readline().strip()))
for i in range(10000):
    try:
        data = int(sys.stdin.readline().strip())
        tmp = root  # 노드
        while tmp:
            if data < tmp.data:
                if tmp.left:
                    tmp = tmp.left
                else:
                    tmp.left = Node(data)
                    break
            elif data > tmp.data:
                if tmp.right:
                    tmp = tmp.right
                else:
                    tmp.right = Node(data)
                    break
    except ValueError:
        break

post_order(root)
