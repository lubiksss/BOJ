N = int(input())
juice_list = [int(input()) for _ in range(N)]
dp = [0]*N

for i in range(N):
    if i==0:
        dp[0] = juice_list[0]
    elif i==1:
        dp[1] = dp[0]+juice_list[1]
    else:
        # 이번차례에 마시지 않는 경우
        a = dp[i-1]
        # 이번차례에 마시고 바로직전에 마시지 않는경우
        b = juice_list[i] + dp[i-2]
        # 이번과 직전에 마시고 그전에는 마시지 않는 경우
        c = juice_list[i] + juice_list[i-1] + dp[i-3]
        dp[i]= max(a,b,c)

print(dp[i])