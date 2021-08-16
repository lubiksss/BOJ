import sys
input = sys.stdin.readline

seq_num = int(input())
num_list = list(map(int, input().split()))
target_num = int(input())
num_list.sort()
cnt = 0

for i in range(seq_num-1):
    left = i+1
    right = seq_num-1
    mtarget_num = target_num - num_list[i]
    while left <= right:
        mid = (left+right) // 2
        if num_list[mid] == mtarget_num:
            cnt += 1
            break
        elif num_list[mid] < mtarget_num:
            left = mid+1
        else:
            right = mid-1

print(cnt)
