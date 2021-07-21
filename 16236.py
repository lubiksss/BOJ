def pm(lista):
    for i in range(len(lista)):
        print(lista[i])
    print('\n')


shark_pos = []
shark_size = 2
shark_eat = 0
next_pos = []
time = 0

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

map_size = int(input())
map = [list(map(int, input().split())) for _ in range(map_size)]

for i in range(map_size):
    for j in range(map_size):
        if map[i][j] == 9:
            shark_pos = [i, j]
            map[i][j] = 0
            
is_update = True
while is_update:
    is_update = False
    # pm(map)
    visit_map = [[0 for _ in range(map_size)]for _ in range(map_size)]
    que = [shark_pos]
    candi = 400


    while que:
        y, x = que.pop(0)
        for i in range(4):
            next_pos = [y, x]
            next_pos[0] = y + dy[i]
            next_pos[1] = x + dx[i]

            if next_pos[0] < 0 or next_pos[0] >= map_size or next_pos[1] < 0 or next_pos[1] >= map_size:
                continue

            if map[next_pos[0]][next_pos[1]] <= shark_size and visit_map[next_pos[0]][next_pos[1]] == 0:
                visit_map[next_pos[0]][next_pos[1]] = visit_map[y][x] + 1
                que.append(next_pos)

    for y in range(map_size):
        for x in range(map_size):
            if map[y][x] < shark_size and map[y][x] != 0 and visit_map[y][x] < candi and visit_map[y][x] != 0:
                candi = visit_map[y][x]
                shark_pos = [y, x]

    if candi < 400:
        map[shark_pos[0]][shark_pos[1]] = 0
        time += visit_map[shark_pos[0]][shark_pos[1]]
        shark_eat += 1
        if shark_eat == shark_size:
            shark_size += 1
            shark_eat = 0
        is_update = True

print(time)
