import sys
import copy
from pprint import pprint
from collections import deque as dq
input = sys.stdin.readline

n, m = map(int,input().split())
maze = [list(map(int,list(input().strip()))) for __ in range(n)]
path = [[0]*m for __ in range(n)]
path[0][0] = 1

def bfs():
    bfs = dq()
    bfs.append([0,0])
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    while bfs:
        basey,basex = bfs.popleft()
        maze[basey][basex] = 0
        for i in range(4):
            nexty = basey+dy[i]
            nextx = basex+dx[i]
            if (nexty<n and nexty>=0) and (nextx<m and nextx>=0) and maze[nexty][nextx] == 1:
                bfs.append([nexty,nextx])
                path[nexty][nextx] = path[basey][basex]+1
                
bfs()
print(path[n-1][m-1])