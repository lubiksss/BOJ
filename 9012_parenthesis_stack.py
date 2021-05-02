import sys

def VPS(string):
    if string =='.':
        return 0

    ps_list = []
    stack_list = []
    flag = 1

    for c in string:
        if c == '(' or c == ')' or c == '[' or c == ']':
            ps_list.append(c)

    for i in range(len(ps_list)):
        if len(ps_list)==0:
            break

        if i == 0 and (ps_list[i] == ')' or ps_list[i] == ']'):
            flag = 0
            break

        if ps_list[i] == '(' or ps_list[i] == '[':
            stack_list.append(ps_list[i])

        elif ps_list[i] == ')':
            if len(stack_list)==0:
                flag = 0
                break

            elif stack_list.pop() != '(':
                flag = 0
                break

        elif ps_list[i] == ']':
            if len(stack_list)==0:
                flag = 0
                break

            elif stack_list.pop() != '[':
                flag = 0
                break

        if i == len(ps_list)-1 and len(stack_list) != 0:
            flag = 0
            break
    
    if flag:
        print('yes')
    else:
        print('no')

string = input()
while(string != '.'):
    VPS(string)
    string = input()