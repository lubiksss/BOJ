from collections import deque as dq
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
tc = 1

while m != 0 or n != 0:
    graph = {}
    for i in range(1, m+1):
        graph[i] = []

    visited = [False] * (m+1)
    que = dq()
    cnt = 0

    for i in range(n):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    for i in range(1, m+1):
        if visited[i]:
            continue
        flag = 1
        # [base, prev]
        que.append([i, 0])
        visited[i] = True

        while que:
            base, prev = que.popleft()
            for next in graph[base]:
                if not visited[next]:
                    que.append([next, base])
                    visited[next] = True
                elif next != prev:
                    flag = 0
        if flag:
            cnt += 1

    if cnt == 0:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')

    m, n = map(int, input().split())
    tc += 1
