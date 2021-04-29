N = int(input())
roads = list(map(int, input().split()))
price = list(map(int, input().split()))

flag = 0
MIN = price[flag]*roads[0]

for i in range(1, N-1):
    if price[i] < price[flag]:
        flag = i
    MIN += price[flag]*roads[i]

print(MIN)