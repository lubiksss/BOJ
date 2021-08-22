import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

LCS = [[0]*(len(a)+1) for __ in range(len(b)+1)]
maxv = 0

for i in range(len(b)+1):
    for j in range(len(a)+1):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif a[j-1] == b[i-1]:
            LCS[i][j] = LCS[i-1][j-1]+1
            maxv = LCS[i][j]
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
            maxv = LCS[i][j]

print(maxv)
# pprint(LCS)

i = len(b)
j = len(a)
tmp = []

while LCS[i][j]:
    if LCS[i][j-1] == LCS[i][j]:
        j -= 1
    elif LCS[i-1][j] == LCS[i][j]:
        i -= 1
    else:
        tmp.append(a[j-1])
        i -= 1
        j -= 1

print(''.join(reversed(tmp)))
