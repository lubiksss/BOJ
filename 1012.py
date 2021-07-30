import sys
from pprint import pprint
from collections import deque as dq
input = sys.stdin.readline

def dfs(starty, startx):
    dfs = dq()
    dfs.append([starty, startx])
    cnt = 0
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while dfs:
        basey, basex = dfs.pop()
        if bmap[basey][basex] == 1:
            bmap[basey][basex] = 0
            cnt += 1
            for i in range(4):
                y = basey+dy[i]
                x = basex+dx[i]
                if (y >= 0 and y < n) and (x >= 0 and x < m):
                    dfs.append([y, x])

    return cnt

tc = int(input())
for __ in range(tc):
    m,n,loc = map(int,input().split())
    bmap = [[0]*m for __ in range(n)]
    for i in range(loc):
        x,y = map(int,input().split())
        bmap[y][x] = 1

    cnt_list = []

    for i in range(n):
        for j in range(m):
            if bmap[i][j] == 1:
                cnt_list.append(dfs(i,j))
    
    print(len(cnt_list))

    