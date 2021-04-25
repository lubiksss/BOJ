import sys
N = int(input())
count = [0]*10001
for i in range(N):
    count[int(sys.stdin.readline())] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i)


