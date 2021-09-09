import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


def preorder(posts, poste, ins, ine):

    if posts > poste or ins > ine:
        return

    root = postorder[poste]

    for i in range(ins, ine+1):
        if root == inorder[i]:
            root_idx = i
            break

    print(root, end=' ')
    # left
    preorder(posts, posts+(root_idx-ins)-1, ins, root_idx-1)
    # right
    preorder(posts+(root_idx-ins), poste-1, root_idx+1, ine)


preorder(0, n-1, 0, n-1)
