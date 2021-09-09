import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


def preorder(postorder, inorder, n):

    if n == 0:
        return
    if n == 1:
        print(postorder[0], end=' ')
        return

    root = postorder[-1]

    for i in range(n):
        if root == inorder[i]:
            root_idx = i

    print(root, end=' ')
    # left
    preorder(postorder[:root_idx], inorder[:root_idx], root_idx)
    # right
    preorder(postorder[root_idx:-1], inorder[root_idx+1:], n-root_idx-1)


preorder(postorder, inorder, n)
