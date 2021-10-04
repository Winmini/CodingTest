import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order(node):
    print(node.data, end='')
    if node.left: pre_order(node.left)
    if node.right: pre_order(node.right)


def in_order(node):
    if node.left: in_order(node.left)
    print(node.data, end='')
    if node.right: in_order(node.right)


def post_order(node):
    if node.left: post_order(node.left)
    if node.right: post_order(node.right)
    print(node.data, end='')


Node_num = int(input())
tree = []


for _ in range(Node_num):
    root, left, right = [i for i in sys.stdin.readline().split()]
    node = Node(root)
    if left != '.': node.left = left
    if right != '.': node.right = right
    tree.append(node)

for i in range(Node_num):
    for j in range(Node_num):
        if tree[i].data == tree[j].left: tree[j].left = tree[i]
        elif tree[i].data == tree[j].right: tree[j].right = tree[i]

pre_order(tree[0])
print()
in_order(tree[0])
print()
post_order(tree[0])