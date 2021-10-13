import re

p = re.compile('(100+1+|01)')

# print(p.findall('10010111'))
# print(p.findall('100000000001101'))

sound = input()
m = p.findall(sound)

sum = 0
for i in m:
    sum += len(i)

if len(sound) == sum:
    print('SUBMARINE')
else:
    print('NOISE')
