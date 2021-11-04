class LRU:
    def __init__(self, max_size):
        self.max_size = max_size
        self.dict = {}

    def put(self, key, value):
        if key in self.dict:
            # 삭제했다가 다시 넣어주어야함.
            self.dict.pop(key)
            # 그리고 넣어줌
        else:
            if len(self.dict) == self.max_size:
                # 딕셔너리 제일앞 지움(제일먼저 들어갔단뜻)
                self.dict.pop(next(iter(self.dict)))
                # 그리고 넣어줌
            else:
                # 딕셔너리 제일뒤에 넣음(제일 최근에 들어갔단뜻)
                # 그냥 넣으면됨
                pass
        self.dict[key] = value


lru = LRU(5)
nlist = range(1, 11, 1)

for number in nlist:
    lru.put(number, '')
    print(lru.dict)
