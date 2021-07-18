from math import sqrt

def is_prime(inta):
    if inta == 0 or inta ==1:
        return False
    s_inta = sqrt(inta)
    # print(s_inta)
    for i in range(2, int(s_inta)+1):
        if inta % i == 0:
            return 0
    return True

# M = 60
# N = 100
M,N = map(int, input().split())

for i in range(M,N+1):
    if is_prime(i) :
        print(i)