from collections import deque as dq


def pl(lista):
    for i in range(len(lista)):
        print(lista[i])
    print('')


def create_area(sy, sx, status, index, count, suma):
    visited = [[0 for _ in range(map_size)]for _ in range(map_size)]
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]

    que = dq([])
    visited[sy][sx] = 1
    que.append([sy, sx])

    while que:
        cury, curx = que.popleft()
        status[cury][curx] = index
        count[index] += 1
        suma[index] += map[cury][curx]

        for i in range(4):
            nexty = cury + dy[i]
            nextx = curx + dx[i]

            if nexty < 0 or nexty >= map_size or nextx < 0 or nextx >= map_size:
                continue

            delta = abs(map[cury][curx] - map[nexty][nextx])

            if visited[nexty][nextx] == 0 and delta >= left and delta <= right:
                visited[nexty][nextx] = 1
                que.append([nexty, nextx])


map_size, left, right = map(int, input().split())
map = [[int(i) for i in input().split()]for _ in range(map_size)]

mi_time = 0
is_update = True

while is_update:
    is_update = False

    status = [[0 for _ in range(map_size)] for _ in range(map_size)]
    area_index = 0
    count = [0 for _ in range(map_size**2+1)]
    suma = [0 for _ in range(map_size**2+1)]

    for y in range(map_size):
        for x in range(map_size):
            if status[y][x] == 0:
                area_index += 1
                create_area(y, x, status, area_index, count, suma)
                # print(y, x)
                # pl(status)

    for y in range(map_size):
        for x in range(map_size):
            # print('in')
            index = status[y][x]
            avg = suma[index] // count[index]
            if map[y][x] != avg:
                map[y][x] = avg
                is_update = True

    if is_update:
        mi_time += 1

print(mi_time)
