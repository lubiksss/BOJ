import sys
input = sys.stdin.readline

n = int(input())
connect = {}
for i in range(1, n+1):
    connect[i] = []

for i in range(1, n+1):
    connect[i].append(int(input()))

sol = []

for i in range(1, n+1):
    que = []
    visited = [False]*(n+1)

    que.append(i)
    visited[i] = True

    while que:
        base = que.pop()
        for next in connect[base]:
            if next == i:
                sol.append(next)
                break
            if not visited[next]:
                que.append(next)
                visited[next] = True

print(len(sol))
for i in sol:
    print(i)
