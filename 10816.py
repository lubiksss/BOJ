import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
num_list2 = list(map(int, input().split()))


def isinlist(x):

    start = 0
    end = len(num_list)-1

    while True:
        mid = (start+end)//2
        if x == num_list[mid]:
            return mid

        elif x > num_list[mid]:
            if mid+1 > end:
                return 500001
            else:
                start = mid+1

        else:
            if mid-1 < start:
                return 500001
            else:
                end = mid-1


def howmany(x, mid):
    if mid == 500001:
        return 0

    else:
        cnt = 1
        lidx = 0
        ridx = 0

        while mid-lidx-1 >= 0 and num_list[mid-lidx-1] == x:
            lidx += 1
            cnt += 1

        while mid+ridx+1 <= n-1 and num_list[mid+ridx+1] == x:
            ridx += 1
            cnt += 1

        return cnt

## 소팅함수가 nlogn
num_list = sorted(num_list)

print(num_list)
for num in num_list2:
    ##logn으로 탐색하고, 좌우로 넓히면서 확인, 최악의경우 n개다확인
    ##그럼 nlong이고
    ##근데 데이터의 갯수만큼 확인하니까 n* nlong인데.. 돌아갈까..
    print(howmany(num, isinlist(num)), end=' ')
