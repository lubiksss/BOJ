def pprint(map):
    for row in map:
        print(row)

map_size = int(input())
map = [list(input()) for __ in range(map_size)]
# pprint(map)

quadtree =''

def divide(map,map_size,num):
    global quadtree
    map_size = map_size

    check_white = 0
    check_blue = 0

    if num == 0:
        quadtree += '('

    for row in map:
        for color in row:
            if color == '0':
                check_white += 1
            else:
                check_blue += 1

    if check_white == 0 or check_blue == 0:
        if check_white == 0:
            quadtree += '1'
        else:
            quadtree += '0'

    else:
        map_size = map_size//2

        # pprint([row[:map_size] for row in map[:map_size]])
        divide([row[:map_size] for row in map[:map_size]],map_size,0)

        # pprint([row[map_size:] for row in map[:map_size]])
        divide([row[map_size:] for row in map[:map_size]],map_size,2)

        # pprint([row[:map_size] for row in map[map_size:]])
        divide([row[:map_size] for row in map[map_size:]],map_size,2)

        # pprint([row[map_size:] for row in map[map_size:]])
        divide([row[map_size:] for row in map[map_size:]],map_size,1)

    if num ==1:
        quadtree += ')'



divide(map,map_size,2)

print(quadtree)