from collections import deque as dq
import sys
input = sys.stdin.readline


def fD(num):
    return num*2 % 10000


def fS(num):
    return (num-1) % 10000


def fL(num):
    return ((num*10)+(num//1000)) % 10000


def fR(num):
    return ((num % 10)*1000 + (num//10)) % 10000


tc = int(input())
for __ in range(tc):
    start, end = map(int, input().split())

    que = dq()
    path = [0]*10000
    visited = [False]*10000

    que.append(start)
    path[start] = 0
    visited[start] = True

    while que:
        v = que.popleft()
        if v == end:
            break

        D = fD(v)
        S = fS(v)
        L = fL(v)
        R = fR(v)

        if visited[D] == False:
            que.append(D)
            path[D] = [0, v]
            visited[D] = True
        if visited[S] == False:
            que.append(S)
            path[S] = [1, v]
            visited[S] = True
        if visited[L] == False:
            que.append(L)
            path[L] = [2, v]
            visited[L] = True
        if visited[R] == False:
            que.append(R)
            path[R] = [3, v]
            visited[R] = True

    idx = end
    tmp = []
    while idx != start:
        if path[idx][0] == 0:
            tmp.append('D')
        elif path[idx][0] == 1:
            tmp.append('S')
        elif path[idx][0] == 2:
            tmp.append('L')
        else:
            tmp.append('R')
        idx = path[idx][1]
    for i in reversed(tmp):
        print(i, end='')
    print()
