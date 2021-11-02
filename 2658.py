import sys
from pprint import pprint
input = sys.stdin.readline

table = [list(map(int, list(input().strip()))) for __ in range(10)]

pprint(table)
