import sys
from collections import deque as dq
input = sys.stdin.readline

vertex_num, edge_num = map(int, input().split())
vertex_start = int(input())
edge_list = [map(int, input().split()) for __ in range(edge_num)]
min_path_list = [600000*10]*(vertex_num+1)
