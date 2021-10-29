import sys
import time
import random


def selection_sort(lista):
    tmp = lista
    for i in range(len(tmp)):
        min = sys.maxsize
        idx = i
        for j in range(i, len(tmp)):
            if tmp[j] < min:
                idx = j
                min = tmp[j]

        if idx == i:
            continue
        else:
            tmp[i], tmp[idx] = tmp[idx], tmp[i]
    return tmp


def insertion_sort(lista):
    tmp = lista
    for i in range(1, len(tmp)):
        tmpa = tmp[i]
        idx = i
        for j in range(1, i+1):
            if tmpa < tmp[i-j]:
                tmp[i-j+1] = tmp[i-j]
                idx = i-j
        if idx == i:
            continue
        else:
            tmp[idx] = tmpa
    return tmp


def bubble_sort(lista):
    tmp = lista
    for i in range(len(tmp)-1):
        for j in range(len(tmp)-1-i):
            if tmp[j] > tmp[j+1]:
                tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
    return tmp


sort_list = [selection_sort, insertion_sort, bubble_sort]

for sort in sort_list:
    num = 1000
    lista = random.sample(range(num), num)
    start = time.time()
    sort(lista)
    print(f'lista=>1000:\t {time.time()-start}')

    num = 10000
    lista = random.sample(range(num), num)
    start = time.time()
    sort(lista)
    print(f'lista=>10000:\t {time.time()-start}')
