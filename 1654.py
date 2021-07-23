import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num_list = [int(input()) for __ in range(n)]

# O(n)
def cutnum(x):
    tmp= 0
    for num in num_list:
        tmp += num//x
    return tmp

# O(n)
max_num = max(num_list)
start =1
end = max_num
tmp = -1

# O(nlogn)
while start <= end:
    mid = (start+end)//2
    if cutnum(mid) >=m:
        tmp = mid
        start = mid+1
    else:
        end = mid-1

print(tmp)
