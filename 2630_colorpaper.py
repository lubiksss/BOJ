def pprint(paper):
    for row in paper:
        print(row)

paper_size = int(input())
paper = [list(map(int, input().split())) for __ in range(paper_size)]
# pprint(paper)

white_num = 0
blue_num = 0


def cut_paper(paper,paper_size):
    global white_num
    global blue_num
    paper_size = paper_size
    check_white = 0
    check_blue = 0

    for row in paper:
        for color in row:
            if color == 0:
                check_white += 1
            else:
                check_blue += 1

    if check_white == 0 or check_blue == 0:
        if check_white == 0:
            blue_num += 1
        else:
            white_num += 1

    else:
        paper_size = paper_size//2

        # pprint([row[:paper_size] for row in paper[:paper_size]])
        cut_paper([row[:paper_size] for row in paper[:paper_size]],paper_size)

        # pprint([row[paper_size:] for row in paper[:paper_size]])
        cut_paper([row[paper_size:] for row in paper[:paper_size]],paper_size)

        # pprint([row[:paper_size] for row in paper[paper_size:]])
        cut_paper([row[:paper_size] for row in paper[paper_size:]],paper_size)

        # pprint([row[paper_size:] for row in paper[paper_size:]])
        cut_paper([row[paper_size:] for row in paper[paper_size:]],paper_size)



cut_paper(paper,paper_size)

print(white_num)
print(blue_num)
