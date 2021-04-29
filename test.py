N = int(input())
listn = list(map(int,input().split()))
listn = sorted(listn)

print(listn[0]*listn[-1])