import sys
from pprint import pprint
from collections import deque as dq
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip('\n'))) for __ in range(n)]


def dfs(starty, startx):
    dfs = dq()
    dfs.append([starty, startx])
    cnt = 0
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while dfs:
        basey, basex = dfs.pop()
        if map[basey][basex] == 1:
            map[basey][basex] = 0
            cnt += 1
            for i in range(4):
                y = basey+dy[i]
                x = basex+dx[i]
                if (y >= 0 and y < n) and (x >= 0 and x < n):
                    dfs.append([y, x])

    return cnt

cnt_list = []

for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            cnt_list.append(dfs(i, j))

cnt_list.sort()
print(len(cnt_list))
for cnt in cnt_list:
    print(cnt)
