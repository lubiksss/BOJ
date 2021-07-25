import sys
input = sys.stdin.readline

n, k = int(input()), int(input())

def cnt_num(mid):
    cnt = 0
    for i in range(1,n+1):
        cnt += min(n,mid//i)
    return cnt

def sol(start,end,target):
    tmp = -1
    while start <= end:
        mid = (start+end)//2
        if cnt_num(mid) >= target:
            if cnt_num(mid-1) < target:
                tmp = mid
                return tmp
            end = mid -1
        else:
            start = mid+1

print(sol(1,k,k))