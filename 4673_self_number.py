def next_num(int_number):
    len_a = len(str(int_number))
    result = int_number
    for i in range(len_a):
        result += int(str(int_number)[i])
    return result

list_next_num = []
for i in range(10000+1):
    list_next_num.append(next_num(i))     

list_self_num = list(set([i for i in range(10000+1)]) - set(list_next_num))
list_self_num.sort()

for i in list_self_num:
    print(i)