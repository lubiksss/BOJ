import sys
input = sys.stdin.readline

N = int(input())
nlist = []
for __ in range(N):
    nlist.append(tuple(map(int, input().split())))
    # 이부분을 list로 하니까 시간초과가 나옴 tuple이 list보다 계산이 빠르다.
    # nlist.append(list(map(int, input().split())))
nlist.sort()

length = 0
pe = -sys.maxsize

for s, e in nlist:
    if s >= pe:
        length += (e-s)
    else:
        if e > pe:
            length += (e-pe)
    pe = max(e, pe)
print(length)
