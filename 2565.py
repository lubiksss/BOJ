N = int(input())
wire_list = [list(map(int, input().split()))for __ in range(N)]
dp = [1]*N

wire_list = sorted(wire_list, key=lambda x: x[0])

right_list = [x[1] for x in wire_list]

# print(wire_list)
# print(right_list)

for i in range(1,N):
    for j in range(i):
        if right_list[j]<right_list[i]:
            dp[i] = max(dp[i], dp[j]+1)

# print(dp)
# print(max(dp))
print(N-max(dp))