from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
tmp = [-sys.maxsize]
d = [0]*N

for i in range(N):
    if num_list[i] > tmp[-1]:
        tmp.append(num_list[i])
        d[i] = len(tmp)-1
    else:
        idx = bisect_left(tmp, num_list[i])
        tmp[idx] = num_list[i]
        d[i] = idx

lentmp = len(tmp)-1
print(lentmp)
