N = int(input())
number_list =[x for x in map(int, input().split())]
#덧셈, 뺄셈, 곱셈, 나눗셈
operand_list = [x for x in map(int, input().split())]

maxnum = -1000000000
minnum = 1000000000

def back_tracking(number_list, operand_list):
    global maxnum
    global minnum
    #탈출 조건
    if len(number_list)==1:
        if number_list[0] < minnum:
            minnum = number_list[0]
        if number_list[0] > maxnum:
            maxnum = number_list[0]
        # raise Exception('test')
        return
    
    # 후보생성
    candidate = [i for i in range(4) for _ in range(operand_list[i])]

    if candidate != []:
        for operand in candidate:
            #덧셈0
            if operand == 0:
                new_number_list = [number_list[0]+number_list[1]]+number_list[2:]
                new_operand_list = [operand_list[0]-1]+operand_list[1:]
                back_tracking(new_number_list, new_operand_list)
            #뺄셈1
            elif operand == 1:
                new_number_list = [number_list[0]-number_list[1]]+number_list[2:]
                new_operand_list = [operand_list[0]]+[operand_list[1]-1]+operand_list[2:]
                back_tracking(new_number_list, new_operand_list)
            #곱셈2
            elif operand == 2:
                new_number_list = [number_list[0]*number_list[1]]+number_list[2:]
                new_operand_list = operand_list[:2]+[operand_list[2]-1]+operand_list[3:]
                back_tracking(new_number_list, new_operand_list)
            #나눗셈3
            else:
                if number_list[0]*number_list[1] < 0:
                    value = -(abs(number_list[0])//abs(number_list[1]))
                else: value = number_list[0]//number_list[1]
                new_number_list = [value]+number_list[2:]
                new_operand_list = operand_list[:3]+[operand_list[3]-1]
                back_tracking(new_number_list, new_operand_list)
    else:
        return

back_tracking(number_list,operand_list)
print(maxnum)
print(minnum)
