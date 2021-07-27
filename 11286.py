import sys
input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for __ in range(n)]
heap = []

def heapify_up(index):
    child = index
    while child != 0:
        parent = (child-1)//2
        if abs(heap[child]) < abs(heap[parent]):
            heap[child], heap[parent] = heap[parent], heap[child]
            child = parent
        elif abs(heap[child]) == abs(heap[parent]):
            if heap[child] < heap[parent]:
                heap[child], heap[parent] = heap[parent], heap[child]
                child = parent
            else:
                return
        else:
            return

def find_abs_smaller_child(index):
    parent = index
    left_child = parent*2+1
    right_child = parent*2+2
    if left_child<len(heap) and abs(heap[left_child])<abs(heap[parent]):
        parent = left_child
    if right_child<len(heap) and abs(heap[right_child])<abs(heap[parent]):
        parent = right_child
    if left_child<len(heap) and abs(heap[left_child])==abs(heap[parent]):
        if heap[left_child] <heap[parent]:
            parent = left_child
    if right_child<len(heap) and abs(heap[right_child])==abs(heap[parent]):
        if heap[right_child] <heap[parent]:
            parent = right_child
    return parent

def heapify_down(index):
    parent = index
    abs_smaller_child = find_abs_smaller_child(parent)
    while parent != abs_smaller_child:
        heap[parent], heap[abs_smaller_child] = heap[abs_smaller_child], heap[parent]
        parent = abs_smaller_child
        abs_smaller_child = find_abs_smaller_child(parent)

def make_heap():
    for i in range((n-1-1)//2, -1, -1):
        heapify_down(i)

for num in num_list:
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heap[0])
            heap[0] = heap[-1]
            heap.pop()
            heapify_down(0)
    else:
        heap.append(num)
        heapify_up(len(heap)-1)