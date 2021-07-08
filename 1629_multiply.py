a, b, c = map(int, input().split())

def pow(a, b):
    if b == 0:
        return 1%c
    else:
        if b % 2 == 0:
            temp = pow(a, b//2)%c
            return temp*temp%c
        else:
            temp = pow(a, b//2)%c
            return temp*temp*(a%c)%c

print(pow(a, b))
