n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    avg = sum(a[1:])/a[0]
    b = [x for x in a[1:] if x > avg]
    c = f'{round(len(b)/a[0]*100, 3):.3f}%'
    print(c)
