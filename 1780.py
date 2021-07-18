# def pprint(map):
#     for row in map:
#         print(row)

paper_size = int(input())
paper = [list(map(int, input().split())) for __ in range(paper_size)]

zero_num = 0
one_num = 0
mone_num = 0


def cut_paper(paper, paper_size):
    global zero_num
    global one_num
    global mone_num

    paper_size = paper_size

    check_zero = 1
    check_one = 1
    check_mone = 1
    breaker = False

    for row in paper:
        for map_num in row:
            if map_num != paper[0][0]:
                breaker = True
                break
        if breaker:
            break

    if not breaker:
        if paper[0][0] == 0:
            zero_num += 1
        elif paper[0][0] == 1:
            one_num += 1
        else:
            mone_num += 1

    else:
        paper_size = paper_size//3

        for i in range(3):
            for j in range(3):
                # pprint([row[paper_size*(i):paper_size*(i+1)]
                #            for row in paper[paper_size*(j):paper_size*(j+1)]])
                cut_paper([row[paper_size*(i):paper_size*(i+1)]
                           for row in paper[paper_size*(j):paper_size*(j+1)]],
                          paper_size)


cut_paper(paper, paper_size)

print(mone_num)
print(zero_num)
print(one_num)
