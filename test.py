from typing import Counter
a = [1, 2, 1, 0, 0, 0, 1]


def count(list):
    cnt = 0
    for e in list:
        if e != 0:
            cnt += 1
    return cnt


print(count(a))
