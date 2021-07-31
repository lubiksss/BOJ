from collections import deque as dq
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

def bfs(n,k):
    que = dq()
    visited = [1]*100001
    que.append([n,0])

    while que:
        node = que.popleft()
        if node[0] ==k:
            return node[1]
        else:
            if visited[node[0]]:
                visited[node[0]] = 0
                if (node[0]-1>=0 and node[0]-1<=100000) and visited[node[0]-1]:
                    que.append([node[0]-1,node[1]+1])
                if (node[0]+1>=0 and node[0]+1<=100000) and visited[node[0]+1]:
                    que.append([node[0]+1,node[1]+1])
                if (node[0]*2>=0 and node[0]*2<=100000) and visited[node[0]*2]:
                    que.append([node[0]*2,node[1]+1])

print(bfs(n,k))
