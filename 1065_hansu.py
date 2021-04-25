def hansu(int_num):
    if int_num<100:
        return True
    else:
        len_a = len(str(int_num))
        a = []
        for i in range(1,len_a):
            a.append(int(str(int_num)[i])-int(str(int_num)[i-1]))
        if len(set(a))==1:
            return True
        else:
            return False

def hansu_count(int_num):
    a = [hansu(i) for i in range(1,int_num+1)]
    return a.count(True)


print(hansu_count(int(input())))