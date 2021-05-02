from collections import deque as dq

N = int(input())
nlist = [int(input())for __ in range(N)]
nlist = sorted(nlist, reverse=True)


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a


def cd(a):
    nlist = []
    for i in range(1, int(a**(1/2))+1):
        if a % i == 0:
            nlist.append(i)
            if a//i != i:
                nlist.append(a//i)
    nlist.remove(1)
    return sorted(nlist)


difflist = dq()
for i in range(len(nlist)-1):
    for j in range(i+1, len(nlist)):
        difflist.append(nlist[i]-nlist[j])


for i in range(len(difflist)):
    # print(difflist)
    if(len(difflist)>1):
        a = difflist.popleft()
        b= difflist.popleft()
        difflist.insert(0,gcd(a,b))

for cd in cd(difflist[0]):
    print(cd, end=' ')