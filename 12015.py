import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))
lis_list = []
lis_list.append(num_list[0])

def lower_bound(start, end, target):
    while start < end:
        mid = (start+end)//2
        if lis_list[mid] >= target:
            end = mid
        else:
            start = mid+1
    return end

for i in range(1, len(num_list)):
    if num_list[i] > lis_list[-1]:
        lis_list.append(num_list[i])
    else:
        lb = lower_bound(0,len(lis_list),num_list[i])
        lis_list[lb] = num_list[i]

print(len(lis_list))