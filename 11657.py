import sys
input = sys.stdin.readline

vertex_num, edge_num = map(int, input().split())
dist_list = [sys.maxsize] * (vertex_num+1)
dist_list[1] = 0


def make_edge():
    edge_list = []
    for i in range(edge_num):
        start, end, weight = map(int, input().split())
        edge_list.append([start, end, weight])
    return edge_list


def Bellman_Ford(edge_list):
    negative_loop = []
    for i in range(vertex_num):
        for edge in edge_list:
            start, end, weight = edge
            if dist_list[start] != sys.maxsize:
                dist_list[end] = min(dist_list[start]+weight,  dist_list[end])
        if i == vertex_num-2:
            negative_loop.append(dist_list[:])
        if i == vertex_num-1:
            negative_loop.append(dist_list[:])
    return negative_loop


edge_list = make_edge()
negative_loop = Bellman_Ford(edge_list)

if negative_loop[0] == negative_loop[1]:
    for i in negative_loop[1][2:]:
        if i == sys.maxsize:
            print(-1)
        else:
            print(i)
else:
    print(-1)
