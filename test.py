num_list = [1,1,2,2,4,4,5,5]


def lower_bound(start, end, target):
    while start < end:
        mid = (start+end)//2
        if num_list[mid] >= target:
            end = mid
        else:
            start = mid+1
    return end