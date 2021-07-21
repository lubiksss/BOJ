board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(y,x) for y in range(9) for x in range(9) if board[y][x]==0]

def func_candidate(pos):
    candidate = [1,2,3,4,5,6,7,8,9]
    y,x = zeros[pos][0], zeros[pos][1]
    #행에 있는 숫자 빼기
    for i in range(9):
        if board[y][i] in candidate:
            candidate.remove(board[y][i])
    #열에 있는 숫자 빼기
    for i in range(9):
        if board[i][x] in candidate:
            candidate.remove(board[i][x])
    #3x3행렬에 있는 숫자 빼기
    for i in range((y//3)*3,((y//3)+1)*3):
        for j in range((x//3)*3,((x//3)+1)*3):
            if board[i][j] in candidate:
                candidate.remove(board[i][j])
    return candidate

flag = False
def sudoku(pos):
    global flag
    if flag:
        return

    # 탈출 조건
    if pos==len(zeros):
        for row in board:
            print(*row)
        flag = True
        return
    
    # 후보군 설정
    candidate = func_candidate(pos)
    
    # 후보가 있다면 후보 넣고 재귀
    if candidate != []:
        for i in candidate:
            board[zeros[pos][0]][zeros[pos][1]] = i
            sudoku(pos+1)
            board[zeros[pos][0]][zeros[pos][1]] = 0
    else:
        return

sudoku(0)
