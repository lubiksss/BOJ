T = int(input())
for i in range(T):
    N = int(input())
    itemlist = [list(input().split()) for __ in range(N)]
    itemdict = {}
    lenlist = []
    base = 1

    for item in itemlist:
        name, itype = item[0], item[1]
        if itype in itemdict:
            itemdict[itype].append(name)
        else:
            itemdict[itype] = [name]

    for item in itemdict:
        lenlist.append(len(itemdict[item]))

    for i in lenlist:
        base = base*(i+1)

    print(base-1)
