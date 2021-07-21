N = int(input())
num_list = list(map(int, input().split()))
MAX = 1

for k in range(1,N+1):
    dp = [1]*N
    for i in range(1,k):
        for j in range(i):
            if num_list[i]>num_list[j]:
                dp[i] = max(dp[i], dp[j]+1)
    for i in range(k,N):
        for j in range(i):
            if num_list[i]<num_list[j]:
                dp[i] = max(dp[i], dp[j]+1)
    MAX = max(max(dp),MAX)

# print(num_list)
# print(dp)
print(MAX)