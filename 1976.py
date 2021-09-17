import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [0]*(N+1)
for i in range(N+1):
    parent[i] = i


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a == b:
        return
    parent[b] = a


for i in range(N):
    con_list = list(map(int, input().split()))
    for j in range(N):
        if con_list[j] == 1:
            union(i+1, j+1)


city_list = list(map(int, input().split()))
tmp = set()
for city in city_list:
    # Union 된 city라고 해서 같은 parent를 가지고 있는것은 아님.
    # 하지만 find로 최상위 root를 찾으면 같음.
    tmp.add(find(parent[city]))

if(len(tmp) == 1):
    print("YES")
else:
    print("NO")
