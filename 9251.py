a = input()
b = input()
MAX = 0

ab = [[0]*(len(a)+1) for __ in range(len(b)+1)]


for y in range(len(b)+1):
    for x in range(len(a)+1):
        if y < len(b) and x < len(a):
            if a[x] == b[y]:
                ab[y+1][x+1] = ab[y][x]+1
            else:
                ab[y+1][x+1] = max(ab[y+1][x], ab[y][x+1])


for i in ab:
    MAX = max(MAX, max(i))

print(MAX)
