from collections import deque as dq
import sys
input = sys.stdin.readline


def DSLR(num, button):
    if button == 'D':
        result = 2*num
        if result > 9999:
            result = result % 10000
    elif button == 'S':
        result = num-1
        if result == 0:
            result = 9999
    elif button == 'L':
        result = int(str(num).zfill(4)[1:] + str(num).zfill(4)[0])
    elif button == 'R':
        result = int(str(num).zfill(4)[3] + str(num).zfill(4)[:3])
    return result


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

        D = DSLR(v, 'D')
        S = DSLR(v, 'S')
        L = DSLR(v, 'L')
        R = DSLR(v, 'R')

        if visited[D] == False:
            que.append(D)
            path[D] = ['D', v]
            visited[D] = True
        if visited[S] == False:
            que.append(S)
            path[S] = ['S', v]
            visited[S] = True
        if visited[L] == False:
            que.append(L)
            path[L] = ['L', v]
            visited[L] = True
        if visited[R] == False:
            que.append(R)
            path[R] = ['R', v]
            visited[R] = True

    idx = end
    tmp = ''
    while idx != start:
        tmp += path[idx][0]
        idx = path[idx][1]
    print(''.join(reversed(tmp)))
