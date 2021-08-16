import sys
input = sys.stdin.readline

seq_num = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
target_num = int(input())

left, right = 0, seq_num - 1
cnt = 0

while left != right:
    tmp = num_list[left]+num_list[right]
    if tmp == target_num:
        left += 1
        cnt += 1
    elif tmp < target_num:
        left += 1
    else:
        right -= 1

print(cnt)
