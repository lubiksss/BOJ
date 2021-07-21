n = int(input())
MOD = 1000000007

piv_mat = [[1, 1], [1, 0]]


def mat_pow(mat, num):
    if num == 1:
        temp = [[1, 0], [0, 1]]
        return mat_mul(mat, temp)
    else:
        temp = mat_pow(mat, num//2)
        if num % 2 == 0:
            return mat_mul(temp, temp)
        else:
            temp2 = mat_mul(temp, temp)
            return mat_mul(mat, temp2)


def mat_mul(mat1, mat2):
    temp = [[0 for __ in range(2)]for __ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] = (temp[i][j] % MOD + (mat1[i][k] %
                                                  MOD * mat2[k][j] % MOD) % MOD) % MOD
    return temp


print(mat_pow(piv_mat, n)[0][1])
