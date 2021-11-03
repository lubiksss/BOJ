import random

nlist = random.sample(range(1, 11), 10)
print(nlist)


def swap(nlist, a, b):
    nlist[a], nlist[b] = nlist[b], nlist[a]


def selection_sort(nlist):
    for i in range(len(nlist)):
        idx = i
        for j in range(i, len(nlist)):
            if nlist[idx] > nlist[j]:
                idx = j
        swap(nlist, i, idx)
    return nlist


def insertion_sort(nlist, start=0, gap=1):
    for i in range(start+gap, len(nlist), gap):
        for j in range(i, start, -gap):
            if nlist[j] < nlist[j-gap]:
                swap(nlist, j, j-gap)
            else:
                break
    return nlist


def bubble_sort(nlist):
    for i in range(len(nlist)):
        for j in range(len(nlist)-i-1):
            if nlist[j] > nlist[j+1]:
                swap(nlist, j, j+1)
    return nlist


def shell_sort(nlist):
    gap = len(nlist)//2
    while gap > 0:
        for i in range(gap):
            insertion_sort(nlist, i, gap)
        gap = gap//2
    return nlist


def merge_sort(nlist, left, right):
    # left포함, right포함
    if left == right:
        return
    if left < right:
        mid = (left+right)//2
        # 왼쪽에다가 한개 더넣는다.
        merge_sort(nlist, left, mid)
        merge_sort(nlist, mid+1, right)

        sorted = [0]*len(nlist)
        ls = left
        le = mid
        rs = mid+1
        re = right
        idx = left
        # 한칸씩 확인함.
        while ls <= le and rs <= re:
            if nlist[ls] <= nlist[rs]:
                sorted[idx] = nlist[ls]
                ls += 1
            else:
                sorted[idx] = nlist[rs]
                rs += 1
            idx += 1
        # 왼쪽 다넣음. 그럼 오른쪽 그대로넣자.
        if rs <= re:
            for i in range(rs, re+1):
                sorted[idx] = nlist[i]
                idx += 1
        # 오른쪽 다넣음. 그럼 왼쪽 그대로넣자.
        if ls <= le:
            for i in range(ls, le+1):
                sorted[idx] = nlist[i]
                idx += 1
        for i in range(left, right+1):
            nlist[i] = sorted[i]
    return nlist


def quick_sort(nlist, left, right):
    # left포함, right포함
    if left >= right:
        return

    pivot = left
    ls = left+1
    rs = right
    while ls <= rs:
        while ls <= right and nlist[ls] <= nlist[pivot]:
            ls += 1
        while rs > left and nlist[rs] >= nlist[pivot]:
            rs -= 1
        if ls < rs:
            swap(nlist, ls, rs)
        else:
            swap(nlist, pivot, rs)
    quick_sort(nlist, left, rs-1)
    quick_sort(nlist, rs+1, right)
    return nlist


print(quick_sort(nlist, 0, len(nlist)-1))
