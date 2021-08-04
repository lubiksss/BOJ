import sys
a = [1, 2, 3, 4]
# b = [1, 2, 3, 4, 5]
print(sys.getsizeof(a))
print(id(a))


def test(a):
    print(sys.getsizeof(a))
    print(id(a))


test(a)
