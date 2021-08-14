import sys
input = sys.stdin.readline

vertex_num, edge_num = int(input()), int(input())
dist_list = [[sys.maxsize] * (vertex_num) for __ in range(vertex_num)]

for i in range(vertex_num):
    dist_list[i][i] = 0

for i in range(edge_num):
    start, end, weight = map(int, input().split())
    if dist_list[start-1][end-1] == sys.maxsize:
        dist_list[start-1][end-1] = weight
    else:
        dist_list[start-1][end-1] = min(weight, dist_list[start-1][end-1])

for mid in range(vertex_num):
    for row in range(vertex_num):
        for col in range(vertex_num):
            dist_list[row][col] = min(
                dist_list[row][col], dist_list[row][mid]+dist_list[mid][col])

for row in dist_list:
    for dist in row:
        if dist == sys.maxsize:
            print(0, end=' ')
        else:
            print(dist, end=' ')
    print()
