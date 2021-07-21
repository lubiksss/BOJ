N = int(input())
tri_list = [list(map(int,input().split())) for __ in range(N)]

dp = [[0]*(i+1) for i in range(N)]

for row in range(N):
    if row ==0:
        dp[0][0] = tri_list[0][0]
    else:
        for i in range(row+1):
            if i==0:
                dp[row][i] = dp[row-1][i] + tri_list[row][i]
            elif i==row:
                dp[row][i] = dp[row-1][i-1] + tri_list[row][i]
            else:
                a = dp[row-1][i-1]
                b = dp[row-1][i]
                dp[row][i] = max(a,b) + tri_list[row][i]

print(max(dp[N-1]))