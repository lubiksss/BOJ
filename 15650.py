def nmfunc(sol, N, M):
    # 탈출 조건
    if(len(sol)==M):
        sollist.append(sol.copy())
        return 0

    # 다음 후보군 생성 과정
    candidate = []
    for i in range(1,N+1):
        if(i>sol[-1]):
            candidate.append(i)

    # 후보군이 있다면 추가하여 재귀함수 실행
    # 만약 탈출하지 못했다면 그거 빼고 다시 한번더
    if candidate != []:
        for i in candidate:
            sol.append(i)
            nmfunc(sol,N,M)
            sol.pop()
    else:
        return 0

N, M = map(int, input().split())
sollist = []
for i in range(1,N+1):
    nmfunc([i], N, M)

for i in sollist:
    print(' '.join(map(str,i)))
