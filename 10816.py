import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
num_list2 = list(map(int, input().split()))

def lower_bound(start, end, target):
    tmp = -1
    while start <= end:
        mid = (start+end)//2
        if num_list[mid] == target:
            tmp = mid
            end = mid-1
        elif target > num_list[mid]:
            start = mid+1
        else:
            end = mid-1
    return tmp
        
def upper_bound(start, end, target):
    tmp = -1
    while start <= end:
        mid = (start+end)//2
        if num_list[mid] == target:
            tmp = mid
            start = mid+1
        elif target > num_list[mid]:
            start = mid+1
        else:
            end = mid-1
    return tmp

num_list.sort()

for num in num_list2:
    ub = upper_bound(0,n-1,num)
    lb = lower_bound(0,n-1,num)

    if ub<0:
        print(0, end = ' ')
    else:
        print(ub-lb+1, end = ' ')
