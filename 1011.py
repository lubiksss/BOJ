# dis = 17
T = int(input())
for T in range(T):
    start, end = map(int, input().split())
    dis = end - start
    rest_dis = dis
    n = 0

    for i in range(1, dis+1):
        if rest_dis == 0:
            break
        if rest_dis - (2*i) >= 0:
            rest_dis = rest_dis - 2*i
            n +=2
            # print(f'{i}씩 양옆에서 움직여서',f'({rest_dis+2*i} => {rest_dis})',f'{n}번 움직임')
        elif rest_dis <= i:
            n+=1
            break
        else:
            n+=2
            break

    print(n)