import sys
import math
input = sys.stdin.readline


N = int(input())
prime_list = [False, False] + [True]*(N-1)
for i in range(int(N**0.5)+1):
    if prime_list[i]:
        for j in range(i+i, N+1, i):
            prime_list[j] = False
prime_list = [num for num in range(2, N+1) if prime_list[num] == True]

left, right = 0, 0
cnt = 0

while right <= len(prime_list):
    temp_sum = sum(prime_list[left:right])
    if temp_sum == N:
        cnt += 1
        right += 1
    elif temp_sum < N:
        right += 1
    else:
        left += 1

print(cnt)
