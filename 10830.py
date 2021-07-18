a, b = map(int, input().split())
mat = [list(map(int, input().split())) for __ in range(a)]

DIVISOR = 1000


def mprint(matrix):
    for row in matrix:
        for e in row:
            print(e, end=' ')
        print()


def mat_pow(mat, num):
    if num == 1:
        temp = [[1  if x==y else 0 for x in range(a)]for y in range(a)]
        return mat_mul(mat,temp)
    else:
        temp = mat_pow(mat, num//2)
        if num % 2 == 0:
            return mat_mul(temp, temp)
        else:
            temp2 = mat_mul(temp, temp)
            return mat_mul(mat, temp2)


def mat_mul(mat1, mat2):
    temp = [[0 for __ in range(a)]for __ in range(a)]
    for i in range(a):
        for j in range(a):
            for k in range(a):
                temp[i][j] = (temp[i][j] % DIVISOR + (mat1[i][k] %
                              DIVISOR * mat2[k][j] % DIVISOR) % DIVISOR) % DIVISOR
    return temp


mprint(mat_pow(mat, b))
