import sys
from pprint import pprint
input = sys.stdin.readline


def make_dist(n, m):
    dist = [[sys.maxsize]*n for __ in range(n)]
    prev = [[-1]*n for __ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for __ in range(m):
        start, end, weight = map(int, (input().split()))
        dist[start-1][end-1] = min(dist[start-1][end-1], weight)
        prev[start-1][end-1] = start
    return dist, prev


def Floyd(dist, prev, n):
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if dist[start][end] > dist[start][mid]+dist[mid][end]:
                    dist[start][end] = dist[start][mid]+dist[mid][end]
                    prev[start][end] = prev[mid][end]


n, m = int(input()), int(input())
dist, prev = make_dist(n, m)
Floyd(dist, prev, n)

for i in range(n):
    for j in range(n):
        if dist[i][j] == sys.maxsize:
            dist[i][j] = 0

dist = [[0 if x == sys.maxsize else x for x in row] for row in dist]

for row in dist:
    print(*row)

for start in range(n):
    for end in range(n):
        if prev[start][end] == -1:
            print(0)
        else:
            tmp = []
            idx = end
            while prev[start][idx] != -1:
                tmp.append(idx+1)
                idx = prev[start][idx]-1
            tmp.append(start+1)
            print(len(tmp), end=' ')
            print(*reversed(tmp))
