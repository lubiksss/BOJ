import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
roots = [0] * (n+1)


def preorder(posts, poste, ins, ine):

    if posts > poste or ins > ine:
        return

    root = postorder[poste]

    root_idx = roots[root]
    print(root, end=' ')
    # left
    preorder(posts, posts+(root_idx-ins)-1, ins, root_idx-1)
    # right
    preorder(posts+(root_idx-ins), poste-1, root_idx+1, ine)


for i in range(n):
    roots[inorder[i]] = i
preorder(0, n-1, 0, n-1)
