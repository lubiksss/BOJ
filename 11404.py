from pprint import pprint
import sys
input = sys.stdin.readline

vertex_num, edge_num = int(input()), int(input())


def make_dist(vertex_num, edge_num):
    dist_list = [[sys.maxsize] * (vertex_num) for __ in range(vertex_num)]
    prev_list = [[-1] * (vertex_num) for __ in range(vertex_num)]
    for i in range(vertex_num):
        dist_list[i][i] = 0

    for i in range(edge_num):
        start, end, weight = map(int, input().split())
        if weight < dist_list[start-1][end-1]:
            dist_list[start-1][end-1] = weight
            prev_list[start-1][end-1] = start
    return dist_list, prev_list


def Floyd_Warshall(vertex_num, dist_list):
    for mid in range(vertex_num):
        for row in range(vertex_num):
            for col in range(vertex_num):
                if dist_list[row][col] > dist_list[row][mid]+dist_list[mid][col]:
                    dist_list[row][col] = dist_list[row][mid] + \
                        dist_list[mid][col]
                    prev_list[row][col] = prev_list[mid][col]


dist_list, prev_list = make_dist(vertex_num, edge_num)
Floyd_Warshall(vertex_num, dist_list)
pprint(prev_list)


for row in dist_list:
    for dist in row:
        if dist == sys.maxsize:
            print(0, end=' ')
        else:
            print(dist, end=' ')
    print()

# prev_list에서 최단경로 뽑는 과정
path_list = [[-1]*vertex_num for __ in range(vertex_num)]
for row in range(vertex_num):
    for col in range(vertex_num):
        path_list[row][col] = []
        path_list[row][col].append(col+1)
        start = row
        end = col
        while start != end:
            path_list[row][col].append(prev_list[start][end])
            end = prev_list[start][end] - 1

for i in range(vertex_num):
    for j in range(vertex_num):
        print(f'{i+1}=>{j+1}경로: {list(reversed(path_list[i][j]))}')
