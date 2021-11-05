import time
import random


class node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class LRU:
    def __init__(self, max_size):
        self.max_size = max_size
        self.dict = {}
        self.dict['head'] = node('head')
        self.dict['tail'] = node('tail')
        self.dict['head'].next = self.dict['tail'].key
        self.dict['tail'].prev = self.dict['head'].key

    def put(self, node):
        if node.key in self.dict:
            # 삭제했다가 다시 넣어주어야함.
            self.dict[self.dict[node.key].prev].next = self.dict[node.key].next
            self.dict[self.dict[node.key].next].prev = self.dict[node.key].prev
            # 그리고 넣어줌
        else:
            if len(self.dict)-2 == self.max_size:
                # 딕셔너리 제일앞 지움(제일 오래 되었다는 뜻)
                tmp = self.dict['head'].next

                self.dict['head'].next = self.dict[self.dict['head'].next].next
                self.dict[self.dict['head'].next].prev = self.dict['head'].key

                self.dict.pop(self.dict[tmp].key)
                # 그리고 넣어줌
            else:
                # 딕셔너리 제일뒤에 넣음(제일 최근에 들어갔단뜻)
                # 그냥 넣으면 됨
                pass

        self.dict[node.key] = node

        self.dict[node.key].prev = self.dict[self.dict['tail'].prev].key
        self.dict[self.dict['tail'].prev].next = node.key

        self.dict['tail'].prev = node.key
        self.dict[node.key].next = self.dict['tail'].key


# lru = LRU(5)
# page = [1, 2, 3, 2, 3, 4, 3, 1, 5, 2, 6, 7, 8]
# for i in page:
#     lru.put(node(i))


# key = 'head'

# while key != None:
#     print(f'prev: {lru.dict[key].prev}')
#     print(f'key: {lru.dict[key].key}')
#     print(f'next: {lru.dict[key].next}')
#     print()
#     key = lru.dict[key].next

# 결과: 5, 2, 6, 7, 8

lru = LRU(10)

page = []
for i in range(1, 100):
    page.append(random.randint(1, 11))
start = time.time()
for i in page:
    lru.put(node(i))
print(f'LRU\tn=100\t\ttime: {time.time()-start:.5f}')

page = []
for i in range(1, 1000):
    page.append(random.randint(1, 11))
start = time.time()
for i in page:
    lru.put(node(i))
print(f'LRU\tn=1000\t\ttime: {time.time()-start:.5f}')

page = []
for i in range(1, 10000):
    page.append(random.randint(1, 11))
start = time.time()
for i in page:
    lru.put(node(i))
print(f'LRU\tn=10000\t\ttime: {time.time()-start:.5f}')

page = []
for i in range(1, 100000):
    page.append(random.randint(1, 11))
start = time.time()
for i in page:
    lru.put(node(i))
print(f'LRU\tn=100000\ttime: {time.time()-start:.5f}')

page = []
for i in range(1, 1000000):
    page.append(random.randint(1, 11))
start = time.time()
for i in page:
    lru.put(node(i))
print(f'LRU\tn=1000000\ttime: {time.time()-start:.5f}')

page = []
for i in range(1, 10000000):
    page.append(random.randint(1, 11))
start = time.time()
for i in page:
    lru.put(node(i))
print(f'LRU\tn=10000000\ttime: {time.time()-start:.5f}')
