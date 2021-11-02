import sys
input = sys.stdin.readline

sol = []


def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


for __ in range(int(input())):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    for __ in range(int(input())):
        cx, cy, r = map(int, input().split())
        if dist(x1, y1, cx, cy) < r:
            if dist(x2, y2, cx, cy) < r:
                pass
            else:
                cnt += 1
        if dist(x2, y2, cx, cy) < r:
            if dist(x1, y1, cx, cy) < r:
                pass
            else:
                cnt += 1
    sol.append(cnt)

for i in sol:
    print(i)
