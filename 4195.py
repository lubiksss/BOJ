import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    # 부모노드를 최상단 루트로 바꿔줌.
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a == b:
        return
    parent[a] = b
    #  위의 뜻은 b 아래에 a가 붙었단뜻이니
    #  b의 그룹개수 + 원래 a가 가지고 있던 그룹개수를 하면
    #  b의 최종 그룹개수가 됨.
    time[b] += time[a]


for __ in range(int(input())):
    F = int(input())
    parent = {}
    time = {}
    for __ in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            time[a] = 1
        if b not in parent:
            parent[b] = b
            time[b] = 1
        union(a, b)
        print(time[find(a)])
