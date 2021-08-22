import sys
input = sys.stdin.readline

N = int(input())
piv = [0, 1] + [-1]*(N-1)

for i in range(2, N+1):
    piv[i] = piv[i-1]+piv[i-2]

print(piv[N])
