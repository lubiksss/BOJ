heap = [5,4,3,2,1,6]
print(heap)

def heapify_up(index):
    child = index
    while child != 0:
        parent = (child-1)//2
        if heap[child] > heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]
            child = parent
        else:
            return


heapify_up(4)

print(heap)