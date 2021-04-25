def make_list(stra):
    al = 'abcdefghijklmnopqrstuvwxyz'
    b = [[] for i in range(len(al))]
    for alphabet in al:
        for i in range(len(stra)):
            if stra[i] == alphabet:
                b[al.index(alphabet)].append(i)
    return(b)


def con_list(lista):
    if lista == [] or len(lista) == 1:
        return True
    for i in range(1, len(lista)):
        if lista[i] - lista[i-1] != 1:
            return False
    return True


def is_group_word(stra):
    b = make_list(stra)
    c = list(map(con_list, b))
    if False in c:
        return False
    else:
        return True


a = []
n = int(input())
for i in range(n):
    a.append(input())

b = list(map(is_group_word, a))
print(b.count(True))
    