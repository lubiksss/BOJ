import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = [1]*N
prev = [-1]*N

for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j]+1)
            if dp[i] == dp[j]+1:
                prev[i] = j

maxn = max(dp)
idx = dp.index(maxn)
tmp = []
while idx != -1:
    tmp.append(num_list[idx])
    idx = prev[idx]

print(maxn)
print(*(reversed(tmp)))
