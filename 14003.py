from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
tmp = [-sys.maxsize]
path = [0]*N

for i in range(N):
    if num_list[i] > tmp[-1]:
        tmp.append(num_list[i])
        path[i] = len(tmp)-1
    else:
        idx = bisect_left(tmp, num_list[i])
        tmp[idx] = num_list[i]
        path[i] = idx

lentmp = len(tmp)-1
print(lentmp)
path = []

for i in range(N-1, -1, -1):
    if path[i] == lentmp:
        path.append(num_list[i])
        lentmp -= 1
print(*reversed(path))
