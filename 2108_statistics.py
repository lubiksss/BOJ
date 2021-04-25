from collections import Counter
import sys

N= int(sys.stdin.readline())
numberlist = []
for _ in range(N):
    numberlist.append(int(sys.stdin.readline()))

def average(numberlist):
    print(int(round(sum(numberlist)/len(numberlist),0)))

def median(numberlist):
    numberlist.sort()
    print(numberlist[int((len(numberlist)/2)-0.5)])

def most(numberlist):
    cnt = Counter(numberlist).most_common()
    if(len(cnt)>1):
        if cnt[0][1] == cnt[1][1]:
            print(cnt[1][0])
        else:
            print(cnt[0][0])
    else:
        print(cnt[0][0])


def range1(numberlist):
    print(max(numberlist)-min(numberlist))


average(numberlist)
median(numberlist)
most(numberlist)
range1(numberlist)