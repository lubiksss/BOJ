import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree_list = list(map(int,input().split()))

def cut_len(height):
    tmp = 0
    for tree in tree_list:
        cut_len = tree-height
        if cut_len>0:
            tmp += cut_len
    return tmp

start = 1
end = max(tree_list)
tmp = 0

while start <= end:
    mid = (start+end)//2
    if cut_len(mid) >= m:
        tmp = mid
        start = mid+1
    else:
        end = mid-1

print(tmp)
