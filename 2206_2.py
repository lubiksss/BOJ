import sys
from copy import deepcopy
from collections import deque as dq
from pprint import pprint
input = sys.stdin.readline

n,m = map(int,input().split())
maze = [list(map(int,input().strip())) for __ in range(n)]
visited = [[[0]*m for __ in range(n)] for __ in range(2)]
visited[1][0][0] = 1
visited[0][0][0] = 1

def bfs():
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    que = dq()
    que.append([1,0,0])
    while que:
        wall,basey,basex = que.popleft()
        if (basey == n-1) and (basex == m-1):
            return visited[wall][basey][basex]
        for i in range(4):
            nexty = basey +dy[i]
            nextx = basex +dx[i]
            if (nexty>=0 and nexty<n) and (nextx>=0 and nextx<m):
                if maze[nexty][nextx] == 1 and wall == 1:
                    visited[0][nexty][nextx] = visited[1][basey][basex]+1
                    que.append([0,nexty,nextx])
                elif maze[nexty][nextx] == 0 and visited[wall][nexty][nextx] ==0:
                    visited[wall][nexty][nextx] = visited[wall][basey][basex]+1
                    que.append([wall,nexty,nextx])
    return -1

print(bfs())