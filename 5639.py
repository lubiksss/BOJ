import sys
from collections import deque as dq
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


# 트리순회는 별다른 조건없이 모든 노드를 다 순회하므로 시간복잡도 N이다.
def postorder(chr):
    if graph[chr][0] != '.':
        postorder(graph[chr][0])
    if graph[chr][1] != '.':
        postorder(graph[chr][1])
    print(chr)


# 입력에 대한 길이가 없기 때문에 EOF를 받을 때까지 입력을 받는다.
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break
graph = {}
for parent in preorder:
    graph[parent] = []

start = 0
end = len(preorder)-1


# 총 시간복잡도 NlogN
def make_tree(start, end):
    parent = preorder[start]
    idx = end
    left = -1
    right = -1
    # parent보다 커지는곳을 찾는 부분의 시간복잡도 N
    while idx > -1 and idx >= start:
        if preorder[idx] < parent:
            left = idx
        if preorder[idx] > parent:
            right = idx
        idx -= 1

    # 하위 left, right트리를 나누는 부분이 logN
    if left == -1 and right == -1:
        graph[parent].append('.')
        graph[parent].append('.')
    elif left == -1:
        graph[parent].append('.')
        graph[parent].append(preorder[right])
        make_tree(right, end)
    elif right == -1:
        graph[parent].append(preorder[left])
        graph[parent].append('.')
        make_tree(left, end)
    else:
        graph[parent].append(preorder[left])
        graph[parent].append(preorder[right])
        make_tree(left, right-1)
        make_tree(right, end)


make_tree(start, end)
# print(graph)

postorder(preorder[0])

# 이렇게 하게 되면 총 시간복잡도 NlogN + N하게 되어 O(NlogN)인데 시간초과가 나옵니다.
