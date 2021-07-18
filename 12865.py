# from pprint import pprint

N, K = map(int, (input().split()))
item_list = [list(map(int, input().split()))for __ in range(N)]
value_list = [[0]*(K+1) for __ in range(N+1)]

for y in range(1, N+1):
    for x in range(1, K+1):
        if item_list[y-1][0] > x:
            value_list[y][x] = value_list[y-1][x]
        else:
            a = item_list[y-1][1] + value_list[y-1][x-item_list[y-1][0]]
            b = value_list[y-1][x]
            value_list[y][x] = max(a, b)

print(value_list[N][K])