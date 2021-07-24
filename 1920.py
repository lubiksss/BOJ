import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

## 파이썬의 기본 소팅함수의 시간복잡도는 nlogn
num_list = sorted(num_list)

m = int(input())
num_list2 = list(map(int, input().split()))

## 입력을 절반씩 잘라가며 탐색하니 logn
def isinlist(start, end, x):
    tmp = 0
    while start <= end:
        mid = (start+end)//2
        if x == num_list[mid]:
            tmp = 1
            break

        elif x > num_list[mid]:
            start = mid+1

        else:
            end = mid-1
    return tmp


for num in num_list2:
    print(isinlist(0, n-1, num))

## 따라서 코드의 총시간복잡도는 nlogn + logn = nlogn이다.