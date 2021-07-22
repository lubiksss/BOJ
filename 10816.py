import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
num_list2 = list(map(int, input().split()))

def lower_bound(start, end, target):

    while end>start:
        mid = (start+end)//2
        if num_list[mid] >= target:
            end = mid
        else:
            start = mid+1
    return end+1
        
def upper_bound(start, end, target):

    while end>start:
        mid = (start+end)//2
        if num_list[mid] > target:
            end = mid
        else:
            start = mid+1
    return end+1

num_list = sorted(num_list)

for num in num_list2:
    print(upper_bound(0,n, num) - lower_bound(0,n,num), end = ' ')