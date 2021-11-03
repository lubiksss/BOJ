import random

nlist = random.sample(range(1, 11), 10)
print(nlist)


def swap(nlist, a, b):
    nlist[a], nlist[b] = nlist[b], nlist[a]


def selection_sort(nlist):
    for i in range(len(nlist)):
        min_idx = i
        for j in range(i, len(nlist)):
            if nlist[min_idx] > nlist[j]:
                min_idx = j
        swap(nlist, min_idx, i)
    return nlist


def bubble_sort(nlist):
    for i in range(len(nlist)):
        for j in range(len(nlist)-i-1):
            if nlist[j] > nlist[j+1]:
                swap(nlist, j, j+1)
    return nlist


def insertion_sort(nlist, start=0, gap=1):
    for i in range(start+gap, len(nlist), gap):
        for j in range(i, start, -gap):
            if nlist[j] < nlist[j-gap]:
                swap(nlist, j, j-gap)
            else:
                break
    return nlist


def shell_sort(nlist):
    gap = len(nlist)//2
    while gap > 0:
        for i in range(gap):
            insertion_sort(nlist, i, gap)
        gap = gap//2
    return nlist


def merge_sort(nlist, left, right):
    # left,right 포함
    if left == right:
        return
    mid = (left+right)//2
    merge_sort(nlist, left, mid)
    merge_sort(nlist, mid+1, right)

    sorted = [0]*len(nlist)
    idx = left
    ls = left
    le = mid
    rs = mid+1
    re = right

    while ls <= le and rs <= re:
        if nlist[ls] <= nlist[rs]:
            sorted[idx] = nlist[ls]
            ls += 1
        else:
            sorted[idx] = nlist[rs]
            rs += 1
        idx += 1

    if ls <= le:
        for i in range(ls, le+1):
            sorted[idx] = nlist[i]
            idx += 1
    if rs <= re:
        for i in range(rs, re+1):
            sorted[idx] = nlist[i]
            idx += 1
    for i in range(left, right+1):
        nlist[i] = sorted[i]

    return nlist


def quick_sort(nlist, left, right):
    # left,right 포함
    if left >= right:
        return

    pvt = left
    ls = left
    rs = right
    while ls <= rs:
        while ls <= right and nlist[ls] <= nlist[pvt]:
            ls += 1
        while rs > left and nlist[rs] >= nlist[pvt]:
            rs -= 1
        if ls <= rs:
            swap(nlist, ls, rs)
        else:
            swap(nlist, pvt, rs)
    quick_sort(nlist, left, rs-1)
    quick_sort(nlist, rs+1, right)

    return nlist


print(quick_sort(nlist, 0, len(nlist)-1))
