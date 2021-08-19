import sys
input = sys.stdin.readline

N = int(input())
dp = [0, 0, 1, 1] + [sys.maxsize] * (N-3)
path = [0, 0, 1, 1] + [0]*(N-3)

dp[1] = 0

for i in range(4, N+1):
    if i % 6 == 0:
        a = dp[i//3] + 1
        b = dp[i//2] + 1
        c = dp[i-1] + 1
        dp[i] = min(a, b, c)
    elif i % 3 == 0:
        a = dp[i//3] + 1
        b = -1
        c = dp[i-1] + 1
        dp[i] = min(a, c)
    elif i % 2 == 0:
        a = -1
        b = dp[i//2] + 1
        c = dp[i-1] + 1
        dp[i] = min(b, c)
    else:
        a = -1
        b = -1
        c = dp[i-1] + 1
        dp[i] = c

    if dp[i] == a:
        path[i] = i//3
    elif dp[i] == b:
        path[i] = i//2
    else:
        path[i] = i-1


print(dp[N])

idx = N
while idx != 0:
    print(idx, end=' ')
    idx = path[idx]
