import sys
input = sys.stdin.readline


def sol(x):
    x1, y1, x2, y2 = x
    for row in range(x1, x2):
        for col in range(y1, y2):
            sumt[row][col] = 1


sumt = [[0]*100 for __ in range(100)]
ans = 0

for i in range(4):
    sol(map(int, input().split()))

for row in sumt:
    ans += sum(row)

print(ans)
