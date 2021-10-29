import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

# table = [[0]*(2**N) for __ in range(2**N)]


def makeZ(n, r, c, idx):
    if n == 2:
        for i in range(n//2+1):
            for j in range(n//2+1):
                # table[i][j] = idx
                if i == r and j == c:
                    print(idx)
                idx += 1

    elif r < n//2 and c < n//2:
        makeZ(n//2, r, c, idx + (n**2//4)*0)
    elif r < n//2 and c >= n//2:
        makeZ(n//2, r, c-n//2, idx + (n**2//4)*1)
    elif r >= n//2 and c < n//2:
        makeZ(n//2, r-n//2, c, idx + (n**2//4)*2)
    elif r >= n//2 and c >= n//2:
        makeZ(n//2, r-n//2, c-n//2, idx + (n**2//4)*3)


makeZ(2**N, r, c, 0)

# for row in table:
#     print(row)
# print(table[r][c])
