import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num_list = list(map(int, input().split()))

left, right = 0, 0
min_num = sys.maxsize
sum = num_list[0]

while left <= right and left <= N-1 and right <= N-1:
    if sum >= S:
        min_num = min(right-left+1, min_num)
        sum -= num_list[left]
        left += 1
    elif sum < S:
        right += 1
        if right <= N-1:
            sum += num_list[right]

if min_num == sys.maxsize:
    print(0)
else:
    print(min_num)
