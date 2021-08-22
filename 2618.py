import sys
input = sys.stdin.readline


def dist(car_x, car_y, event_x, event_y):
    return abs(car_x-event_x) + abs(car_y-event_y)


N = int(input())
W = int(input())

event = [[1, 1], [N, N]] + [list(map(int, input().split())) for __ in range(W)]
