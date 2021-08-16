import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

left, right = 0, N - 1
min_num = abs(sys.maxsize)
min_pair = []

while left != right:
    tmp = num_list[left]+num_list[right]
    if abs(tmp) < abs(min_num):
        min_num = tmp
        min_pair = [num_list[left], num_list[right]]
    if tmp == 0:
        min_piar = num_list[left], num_list[right]
        break
    elif tmp < 0:
        left += 1
    else:
        right -= 1

print(*min_pair)
