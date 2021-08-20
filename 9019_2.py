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


for __ in range(int(input())):
    start, end = map(int, input().split())

    que = dq()
    path = ['']*10000

    que.append(start)
    # 원래시작점은 아무데서도 오지않았다고 표현하는게 맞지만
    # visited 배열처럼 쓰기위해서 방문했다는 의미로 아무거나 써넣고
    # 나중에 지움.
    path[start] = 'A'

    # 보통 큐가 비지않으면 이라고 썻었는데
    # 큐를 확인할 필요없이 그냥 목적지에 path가 완성되면 바로 break
    while not path[end]:
        v = que.popleft()

        D = fD(v)
        S = fS(v)
        L = fL(v)
        R = fR(v)

        if not path[D]:
            que.append(D)
            path[D] = path[v]+'D'
        if not path[S]:
            que.append(S)
            path[S] = path[v]+'S'
        if not path[L]:
            que.append(L)
            path[L] = path[v]+'L'
        if not path[R]:
            que.append(R)
            path[R] = path[v]+'R'

    print(path[end].lstrip('A'))
