parent = [i for i in range(1, 11)]


def find(a):
    if parent[a] == a:
        return
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[b] = a
