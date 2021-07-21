count = 0

def queen_game(sol, N):
    global count
    #탈출조건
    if(len(sol)==N):
        count += 1
        # print(sol)
        return 0

    #다음 후보군 설정
    candidate = list(range(N))
    for i in sol:
        if i in candidate:
            candidate.remove(i)
    for i in range(len(sol)):
        for j in list(range(N)):
            if abs(sol[i]-j) == abs(i-len(sol)):
                if j in candidate:
                    candidate.remove(j)

    #후보군이 있다면 후보군 넣고 재귀
    if candidate != []:
        for i in candidate:
            sol.append(i)
            queen_game(sol,N)
            sol.pop()
    else:
        return 0

N = int(input())
for i in range(N):
    queen_game([i],N)
print(count)


# answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
# print(answer[int(input())])