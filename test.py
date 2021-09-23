import sys
import time
import random

NUM = 10
lista = random.sample(range(NUM), NUM)
print(lista)


def bubble_sort(lista):
    tmp = lista
    for i in range(len(tmp)-1):
        for j in range(len(tmp)-1-i):
            if tmp[j] > tmp[j+1]:
                tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
    return tmp


print(bubble_sort(lista))
