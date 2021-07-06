from pprint import pprint

paper_size = int(input())
paper = [list(map(int, input().split())) for __ in range(paper_size)]

pprint(paper)

small_paper = [row[:paper_size//2] for row in paper[:paper_size//2]]
pprint(small_paper)
