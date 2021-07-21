import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

## 파이썬의 기본 소팅함수의 시간복잡도는 nlogn
num_list = sorted(num_list)

m = int(input())
num_list2 = list(map(int, input().split()))

## 입력을 절반씩 잘라가며 탐색하니 logn
def isinlist(x):

    start = 0
    end = len(num_list)-1

    while True:
        mid = (start+end)//2
        if x == num_list[mid]:
            return 1

        elif x > num_list[mid]:
            if mid+1 > end:
                return 0
            else:
                start = mid+1

        else:
            if mid-1 <start:
                return 0
            else:
                end = mid-1


for num in num_list2:
    print(isinlist(num))

## 따라서 코드의 총시간복잡도는 nlogn + logn = nlogn이다.