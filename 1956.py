import sys

vertex_num, edge_num = map(int, input().split())
dist_list = [[sys.maxsize]*vertex_num for __ in range(vertex_num)]
cycle = sys.maxsize

for i in range(edge_num):
    start, end, weight = map(int, input().split())
    dist_list[start-1][end-1] = weight

for mid in range(vertex_num):
    for row in range(vertex_num):
        for col in range(vertex_num):
            dist_list[row][col] = min(
                dist_list[row][col], dist_list[row][mid] + dist_list[mid][col])
            if row == col:
                cycle = min(cycle, dist_list[row][col])

if cycle == sys.maxsize:
    print(-1)
else:
    print(cycle)
