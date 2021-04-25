import random
import time
from collections import deque
import math

def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def bubble_sort(n):
    bl = random.sample(range(n),n)
    start = time.time()
    for i in range(n):
        for j in range(n-i-1):
            if (bl[j]>bl[j+1]):
                swap(bl,j,j+1)
    print(f'bubble sort\tlen: {n:5}\ttime: {time.time()-start:20}')

def selection_sort(n):
    sl = random.sample(range(n),n)
    start = time.time()
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if(sl[min]>sl[j]):
                min = j
        swap(sl,i,min)
    print(f'selection sort\tlen: {n:5}\ttime: {time.time()-start:20}')

def partition(ql, left, right):
    pivot = ql[left]
    i = left
    j = right
    
    while(i<j):
        while(pivot<ql[j]):
            j = j-1
        while(i<j and pivot>=ql[i]):
            i = i+1
        swap(ql,i,j)
    ql[left] = ql[i]
    ql[i] = pivot
    return i
 
def quick_sort(ql, left, right):
    if(left>= right):
        return
    pivot = partition(ql, left, right)
    quick_sort(ql,left,pivot-1)
    quick_sort(ql,pivot+1,right)

def insertion_sort(n):
    il = random.sample(range(n),n)
    start = time.time()
    for i in range(1,n):
        for j in range(i,0,-1):
            if(il[j]>=il[j-1]):
                break
            else:
                swap(il,j,j-1)
    print(f'insertion sort\tlen: {n:5}\ttime: {time.time()-start:20}')

def radix_sort(n):
    rl = random.sample(range(n),n)
    baskets = []
    start = time.time()
    for _ in range(10):
        baskets.append(deque())
    
    radix = int(math.log10(max(rl)))
    for i in range(radix+1):
        distribute(rl,baskets,i)
        collect(rl,baskets)
    print(f'radix sort\tlen: {n:5}\ttime: {time.time()-start:20}')

def distribute(n, baskets, radix):
    for num in n:
        basket_num = (num//(10**radix))%10
        baskets[basket_num].append(num)
    # print(baskets)

def collect(n, baskets):
    n.clear()
    for basket in baskets:
        for _ in range(len(basket)):
            n.append(basket.popleft())
    # print(n)

# ql = random.sample(range(10000),10000)
# # print(ql)
# start = time.time()
# quick_sort(ql,0,9999)
# # print(ql)
# print(time.time()-start)
# ql = random.sample(range(100000),100000)
# # print(ql)
# start = time.time()
# quick_sort(ql,0,99999)
# # print(ql)
# print(time.time()-start)
# print(ql)
# # insertion_sort(1000)
# # insertion_sort(10000)

radix_sort(1000)
radix_sort(10000)
radix_sort(100000)
radix_sort(1000000)