
from copy import deepcopy

class Posi:
    x = 0
    y = 0


def pm(lista):
    for i in range(len(lista)):
        print(lista[i])
    print('\n')


def bfs(y, x, index):
    visited = [[0 for _ in range(map_size)]for _ in range(map_size)]
    visited[y][x] = 1
    status[y][x] = index
    que = [[y, x]]
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    while que:
        b, a = que.pop(0)

        for i in range(4):
            next = Posi()
            next.y = b + dy[i]
            next.x = a + dx[i]

            if next.y < 0 or next.y >= map_size or next.x < 0 or next.x >= map_size:
                continue

            delta = abs(map[b][a] - map[next.y][next.x])
            if visited[next.y][next.x] == 0 and delta >= left and delta <= right:
                visited[next.y][next.x] = 1
                status[next.y][next.x] = index
                que.append([next.y, next.x])

map_size, left, right = map(int, input().split())
map = [[int(i) for i in input().split()]for _ in range(map_size)]

is_update = True
number = 0
while is_update:
    is_update = False
    temp = deepcopy(map)
    status = [[0 for _ in range(map_size)]for _ in range(map_size)]
    index = 0
    sum = [0 for _ in range((map_size**2)+1)]
    count = [0 for _ in range((map_size**2)+1)]

    for y in range(map_size):
        for x in range(map_size):
            if status[y][x] == 0:
                index += 1
                bfs(y, x, index)
    # pm(status)

    for y in range(map_size):
        for x in range(map_size):
            for i in range(1,index+1):
                if status[y][x] == i:
                    sum[i] += map[y][x]
                    count[i] +=1

    for y in range(map_size):
        for x in range(map_size):
            map[y][x] = sum[status[y][x]]//count[status[y][x]]
    # pm(map)

    if temp != map:
        is_update = True
        number +=1        

print(number)