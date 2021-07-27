import sys
input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for __ in range(n)]
big_heap = []
small_heap = []

def big_heapify_up(index):
    child = index
    while child != 0:
        parent = (child-1)//2
        if big_heap[child] > big_heap[parent]:
            big_heap[child], big_heap[parent] = big_heap[parent], big_heap[child]
            child = parent
        else:
            return

def big_find_bigger_child(index):
    parent = index
    left_child = parent*2+1
    right_child = parent*2+2
    if left_child<len(big_heap) and big_heap[left_child]>big_heap[parent]:
        parent = left_child
    if right_child<len(big_heap) and big_heap[right_child]>big_heap[parent]:
        parent = right_child
    return parent

def big_heapify_down(index):
    parent = index
    bigger_child = big_find_bigger_child(parent)
    while parent != bigger_child:
        big_heap[parent], big_heap[bigger_child] = big_heap[bigger_child], big_heap[parent]
        parent = bigger_child
        bigger_child = big_find_bigger_child(parent)

def small_heapify_up(index):
    child = index
    while child != 0:
        parent = (child-1)//2
        if small_heap[child] < small_heap[parent]:
            small_heap[child], small_heap[parent] = small_heap[parent], small_heap[child]
            child = parent
        else:
            return

def small_find_smaller_child(index):
    parent = index
    left_child = parent*2+1
    right_child = parent*2+2
    if left_child<len(small_heap) and small_heap[left_child]<small_heap[parent]:
        parent = left_child
    if right_child<len(small_heap) and small_heap[right_child]<small_heap[parent]:
        parent = right_child
    return parent

def small_heapify_down(index):
    parent = index
    smaller_child = small_find_smaller_child(parent)
    while parent != smaller_child:
        small_heap[parent], small_heap[smaller_child] = small_heap[smaller_child], small_heap[parent]
        parent = smaller_child
        smaller_child = small_find_smaller_child(parent)

for num in num_list:
    if len(big_heap) == len(small_heap):
        big_heap.append(num)
        big_heapify_up(len(big_heap)-1)

    else:
        small_heap.append(num)
        small_heapify_up(len(small_heap)-1)

    if len(big_heap)>0 and len(small_heap)>0 and big_heap[0] > small_heap[0]:
        big_heap[0], small_heap[0] =small_heap[0],big_heap[0]
        big_heapify_down(0)
        small_heapify_down(0)

    print(big_heap[0])

    
