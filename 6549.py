import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def max_area(left, right):
    if left == right:
        return hist[left]

    else:
        half_idx = (left+right)//2
        new_left = half_idx
        new_right = half_idx + 1
        new_height = min(hist[new_left], hist[new_right])
        new_width = 2
        temp = 2 * new_height

        while True:
            if (new_left == left or hist[new_left] == 0) and (new_right == right or hist[new_right] == 0):
                break

            elif new_left == left or hist[new_left] == 0:
                new_height = min(new_height,hist[new_right+1])
                new_right +=1
                new_width +=1

            elif new_right == right or hist[new_right] == 0:
                new_height = min(new_height,hist[new_left-1])
                new_left -=1
                new_width +=1

            else:
                if hist[new_left-1] >= hist[new_right+1]:
                    new_height = min(new_height,hist[new_left-1])
                    new_left -=1
                    new_width +=1
                else:
                    new_height = min(new_height,hist[new_right+1])
                    new_right +=1
                    new_width +=1

            temp = max(temp,new_width*new_height)
        
        return max(max_area(left,half_idx),max_area(half_idx+1,right),temp)


while True:
    tc, *hist = list(map(int, input().split()))
    if tc == 0:
        break

    print(max_area(0, tc-1))