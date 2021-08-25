from collections import deque as dq
import sys
input = sys.stdin.readline

N = int(input())

graph = {}
for i in range(N):
    root, left, right = input().split()
    if root not in graph.keys():
        graph[root] = []
    graph[root].append(left)
    graph[root].append(right)


# root first
def preorder(chr):
    print(chr, end='')
    if graph[chr][0] != '.':
        preorder(graph[chr][0])
    if graph[chr][1] != '.':
        preorder(graph[chr][1])


# left tree => root
def inorder(chr):
    if graph[chr][0] != '.':
        inorder(graph[chr][0])
    print(chr, end='')
    if graph[chr][1] != '.':
        inorder(graph[chr][1])


# child(left=>right) => root
def postorder(chr):
    if graph[chr][0] != '.':
        postorder(graph[chr][0])
    if graph[chr][1] != '.':
        postorder(graph[chr][1])
    print(chr, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
