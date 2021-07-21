a = input()
if len(a) == 1:
    a = '0'+a

n = 0
b = a

while True:
    if n != 0 and a == b:
        print(n)
        break
    else:
        if len(a) == 1:
            a = '0'+a
        a = a[1] + str((int(a[0]) + int(a[1]))%10)
        # print(a)
        n += 1
