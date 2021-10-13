import sys
input = sys.stdin.readline

for __ in range(int(input())):
    n = int(input())
    island = []
    for i in range(n):
        island.append(tuple(map(int, input().split())))
    island.sort(key=lambda x: (x[0], -x[1]))

    print(island)

    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if island[i][1] >= island[j][1]:
                cnt += 1

    print(cnt)
