import sys
input = sys.stdin.readline

N = int(input())
tlist = []
for __ in range(N):
    tlist.append(int(input()))

cnt = 1
top = tlist[0]
for t in tlist:
    if t > top:
        cnt += 1
    top = max(t, top)

tlist.reverse()
rcnt = 1
top = tlist[0]
for t in tlist:
    if t > top:
        rcnt += 1
    top = max(t, top)

print(cnt)
print(rcnt)
