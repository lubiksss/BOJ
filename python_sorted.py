import sys
from collections import deque

N = int(sys.stdin.readline())
poslist = []
for i in range(N):
    x,y = sys.stdin.readline().split()
    poslist.append((int(x), y))

# print(poslist)
poslist = sorted(poslist, key = lambda x:x[0])

for i in poslist:
    print(i[0],i[1])