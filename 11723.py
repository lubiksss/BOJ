import sys
input = sys.stdin.readline

S = [0]*21

M = int(input())

for __ in range(M):
    oper = input().strip()
    if oper == 'all':
        S = [1]*21
    elif oper == 'empty':
        S = [0]*21
    else:
        a, b = oper.split()
        b = int(b)
        if a == 'add':
            S[b] = 1
        elif a == 'remove':
            S[b] = 0
        elif a == 'check':
            print(S[b])
        elif a == 'toggle':
            S[b] = (S[b]+1) % 2
