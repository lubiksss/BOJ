N = int(input())
num_list = list(map(int, input().split()))
dp = [0]*N

for i in range(N):
    if i == 0:
        dp[i] = num_list[i]
    else:
        a = dp[i-1] + num_list[i]
        b = num_list[i]
        dp[i] = max(a,b)

print(max(dp))
