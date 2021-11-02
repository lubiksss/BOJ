import sys
input = sys.stdin.readline

N = int(input())

board = [[' ']*((N//3)*5+(N//3-1)) for __ in range(N)]


def star(board, srow, erow, col):
    if (erow-srow) // 2 >= 3:
        star(board, srow, srow+(erow-srow)//2, col)
        star(board, srow+(erow-srow)//2, erow, col-(erow-srow)//2)
        star(board, srow+(erow-srow)//2, erow, col+(erow-srow)//2)
        return
    board[srow][col] = '*'
    board[srow+1][col-1] = '*'
    board[srow+1][col+1] = '*'
    board[srow+2][col-2] = '*'
    board[srow+2][col-1] = '*'
    board[srow+2][col] = '*'
    board[srow+2][col+1] = '*'
    board[srow+2][col+2] = '*'


def print_star(board):
    for row in board:
        print(''.join(row))


star(board, 0, N, len(board[0])//2)

print_star(board)

print(len(board))
print(len(board[0]))
