import sys
from collections import deque as dq
from pprint import pprint
input = sys.stdin.readline

def bfs(start,dest,board_size):
    dy = [-2,-1,+1,+2,+2,+1,-1,-2]
    dx = [+1,+2,+2,+1,-1,-2,-2,-1]

    que = dq()
    visited = [[0]*board_size for __ in range(board_size)]

    que.append([*start,0])

    while que:
        basey,basex,time = que.popleft()
        
        if[basey,basex] == dest:
            return time
        else:
            for i in range(8):
                nexty = basey + dy[i]
                nextx = basex + dx[i]
                if (0<=nexty<board_size) and (0<=nextx<board_size) and visited[nexty][nextx] == 0:
                    que.append([nexty,nextx,time+1])
                    visited[nexty][nextx] = 1
    return -1


tc = int(input())
for __ in range(tc):
    board_size = int(input())
    start = list(map(int,input().split()))
    dest = list(map(int,input().split()))

    print(bfs(start,dest,board_size))