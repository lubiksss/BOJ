import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def makeTree(currentNode, parent):
    for node in connect[currentNode]:
        if node != parent:
            tree[currentNode].append(node)
            makeTree(node, currentNode)


def countSubtreeNodes(currentNode):
    for node in tree[currentNode]:
        countSubtreeNodes(node)
        dp[currentNode] += dp[node]


# input1
N, R, Q = map(int, input().split())
connect = {}
for i in range(1, N+1):
    connect[i] = []
for __ in range(N-1):
    U, V = map(int, input().split())
    connect[U].append(V)
    connect[V].append(U)

# 받은 인풋으로 tree랑 dp만듬
tree = {}
for i in range(1, N+1):
    tree[i] = []
dp = [1] * (N+1)
makeTree(R, -1)
countSubtreeNodes(R)

# input2
for __ in range(Q):
    print(dp[int(input())])
