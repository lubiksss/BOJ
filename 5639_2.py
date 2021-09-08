import sys
from collections import deque as dq
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

# 입력에 대한 길이가 없기 때문에 EOF를 받을 때까지 입력을 받는다.
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break


def post_order(start, end):
    if start > end:
        return
    idx = end+1
    for i in range(start+1, end+1):
        if preorder[start] < preorder[i]:
            idx = i
            break

    post_order(start+1, idx-1)
    post_order(idx, end)
    print(preorder[start])


post_order(0, len(preorder)-1)
