import sys
input = sys.stdin.readline

n = int(input())

nlist = [0]*n
for i in range(n):
    nlist[i] = float(input())

dp = [0]*n
dp[0] = nlist[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]*nlist[i], nlist[i])

print(f'{max(dp):.3f}')
