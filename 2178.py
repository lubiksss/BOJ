from collections import deque as dq
def pm(maze):
    for i in range(len(maze)):
        print(maze[i])
    print('\n')

n, m = map(int, input().split())
maze = [[int(n) for n in input()] for _ in range(n)]
v_maze = [[0 for _ in range(m)]for _ in range(n)]

que = dq([[0,0]])
v_maze[0][0] =1

while que:
    y, x = que.popleft()
    # 위 검색
    if y-1 >=0:
        if maze[y-1][x] ==1 and v_maze[y-1][x] ==0:
            que.append([y-1,x])
            v_maze[y-1][x] = v_maze[y][x]+1
    # 아래쪽
    if y+1 < n:
        if maze[y+1][x] ==1 and v_maze[y+1][x] ==0:
            que.append([y+1,x])
            v_maze[y+1][x] = v_maze[y][x]+1
    # 왼쪽 검색
    if x-1 >= 0:
        if maze[y][x-1] ==1 and v_maze[y][x-1] ==0:
            que.append([y,x-1])
            v_maze[y][x-1] = v_maze[y][x]+1
    # 오른쪽 검색
    if x+1 < m:
        if maze[y][x+1] ==1 and v_maze[y][x+1] ==0:
            que.append([y,x+1])
            v_maze[y][x+1] = v_maze[y][x]+1

pm(maze)
pm(v_maze)
print(v_maze[n-1][m-1])
