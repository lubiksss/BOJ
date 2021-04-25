cl = ['c=','c-','dz=','d-','lj','nj','s=','z=']

a = input()

b = [a.count(i) for i in cl]
b = sum(b)

print(len(a)-b)