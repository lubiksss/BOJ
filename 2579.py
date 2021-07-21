N = int(input())
stair_list = [int(input()) for __ in range(N)]
dp = [0]*N

for i in range(N):
    if i == 0:
        dp[i] = stair_list[0]
    elif i == 1:
        dp[i] = stair_list[i] + dp[0]
    else:
        #지금 계단을 밟고 전계단 안밟고 전전계단 밟는 경우
        a = stair_list[i] + dp[i-2]
        #지금 계단을 밟고 전계단 밟고 전전계단 안밟는 경우
        b = stair_list[i] + stair_list[i-1] + dp[i-3]
        dp[i] = max(a, b)

print(dp[N-1])
