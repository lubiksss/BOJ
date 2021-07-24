import sys
input = sys.stdin.readline

n,c = map(int,input().split())
num_list = [int(input()) for __ in range(n)]

## O(nlogn)
num_list.sort()

def ispossible(mid):
    tmp=1
    start = 0
    for i in range(len(num_list)):
        if num_list[i] - num_list[start] >= mid:
            tmp+=1
            start = i
    return tmp


def cal_max(start, end):
    tmp = -1
    while start <= end:
        mid= (start+end)//2
        if ispossible(mid) >= c:
            tmp = mid
            start = mid+1
        else:
            end = mid-1
    return tmp

start, end = 1,num_list[-1]
print(cal_max(start,end))