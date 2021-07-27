import sys
import heapq
input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for __ in range(n)]
big_heap = []
small_heap = []

for num in num_list:
    if len(big_heap) == len(small_heap):
        heapq.heappush(big_heap, (-num, num))

    else:
        heapq.heappush(small_heap,num)

    if len(big_heap)>0 and len(small_heap)>0 and big_heap[0][1] > small_heap[0]:
        big_tmp = heapq.heappop(big_heap)[1]
        small_tmp = heapq.heappop(small_heap)
        heapq.heappush(big_heap, (-small_tmp,small_tmp))
        heapq.heappush(small_heap, big_tmp)
    print(big_heap[0][1])

    
