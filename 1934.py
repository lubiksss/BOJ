T = int(input())
nlist = [list(map(int, input().split())) for __ in range(T)]

for numbers in nlist:
    a, b = max(numbers[0], numbers[1]), min(numbers[0], numbers[1])
    mab = a*b
    while(b!=0):
        r = a%b
        a = b
        b = r
    print(int(mab/a))