import sys
input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for __ in range(n)]
heap = []

def heapify_up(index):
    child = index
    while child != 0:
        parent = (child-1)//2
        if heap[child] > heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]
            child = parent
        else:
            return

def find_bigger_child(index):
    parent = index
    left_child = parent*2+1
    right_child = parent*2+2
    if left_child<len(heap) and heap[left_child]>heap[parent]:
        parent = left_child
    if right_child<len(heap) and heap[right_child]>heap[parent]:
        parent = right_child
    return parent

def heapify_down(index):
    parent = index
    bigger_child = find_bigger_child(parent)
    while parent != bigger_child:
        heap[parent], heap[bigger_child] = heap[bigger_child], heap[parent]
        parent = bigger_child
        bigger_child = find_bigger_child(parent)

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