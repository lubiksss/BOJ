import sys
from collections import deque as dq
input = sys.stdin.readline

while True:
    tc, *hist = list(map(int, input().split()))
    hist.append(0)
    if tc == 0:
        break
    
    stack = dq()
    max_sq = 0

    for i in range(len(hist)):

        while len(stack)!= 0 and hist[stack[-1]] > hist[i]:
            tmp = stack.pop()

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] -1
            max_sq = max(max_sq, width*hist[tmp])
        stack.append(i)
    
    print(max_sq)
        
