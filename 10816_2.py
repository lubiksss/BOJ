import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
num_list2 = list(map(int, input().split()))

sol = [0]*20000001
OFFSET = 10000000

for num in num_list:
    sol[num+OFFSET] +=1

for num in num_list2:
    print(sol[num+OFFSET], end = ' ')
