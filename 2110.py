import sys
input = sys.stdin.readline

n,c = map(int,input().split())
num_list = [int(input()) for __ in range(n)]

## O(nlogn)
num_list.sort()

def ispossible():
    pass

start, end = 1,num_list[-1]
tmp = -1

while start <= end:
    mid= (start+end)//2
    if ispossible(mid) >= c:
        tmp = mid
        start = mid+1
    else:
        end = mid-1