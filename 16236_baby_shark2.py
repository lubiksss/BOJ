class Shark():
    y = 0
    x = 0
    time = 0
    size = 0
    eat = 0

shark = Shark()

dy = [0,0,-1,+1]
dx = [-1,+1,0,0]

map_size = int(input())
map = [list(map(int, input().split())) for _ in range(map_size)]

for y in range(map_size):
    for x in range(map_size):
        if map[y][x] == 9:
            shark.y = y
            shark.x = x
            shark.time = 0
            shark.size = 2
            shark.eat = 0
            map[y][x] = 0

is_update = True

while is_update:
    is_update = False

    visited = [[False for _ in range(map_size)] for _ in range(map_size)]
    visited[shark.y][shark.x]= True
    que= [shark]

    candi= Shark()
    candi.y= map_size
    candi.time= -1

    while que:
        cur = que.pop(0)
        if candi.time != -1 and candi.time<cur.time :
            break
        if map[cur.y][cur.x] < shark.size and map[cur.y][cur.x] != 0:
            is_update = True
            if candi.y> cur.y or (candi.y == cur.y and candi.x > cur.x):
                candi = cur

        for i in range(4):
            next = Shark()
            next.y = cur.y + dy[i]
            next.x = cur.x + dx[i]
            next.time = cur.time+1

            if next.y<0 or next.y>=map_size or next.x<0 or next.x >=map_size:
                continue

            if visited[next.y][next.x] == False and map[next.y][next.x] <= shark.size:
                visited[next.y][next.x] = True
                que.append(next)

    if is_update:
        shark = candi
        shark.eat +=1
        if shark.eat == shark.size:
            shark.size +=1
            shark.eat = 0
        map[shark.y][shark.x] = 0
print(shark.time)