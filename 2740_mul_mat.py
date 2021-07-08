def mprint(matrix):
    for row in matrix:
        for e in row:
            print(e,end = ' ')
        print()

m, n = map(int,input().split())
x = [list(map(int,input().split()))for __ in range(m)]

m2, n2 = map(int,input().split())
y = [list(map(int,input().split()))for __ in range(m2)]

def mat_mul(mat1, mat2):
    temp = [[0 for __ in range(len(mat2[0]))]for __ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                temp[i][j] += mat1[i][k] * mat2[k][j]
    return temp

mprint(mat_mul(x,y))