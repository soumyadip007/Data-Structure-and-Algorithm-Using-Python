#Required Sol
def solveNQUtil(board, col, N):
    if (col >= N):return True
    for i in range(N):
        if (ld[i - col + N - 1] != 1 and rd[i + col] != 1) and cl[i] != 1:
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
            if solveNQUtil(board, col + 1, N):return True
            board[i][col] = 0  # BACKTRACK
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
    return False

ld = [0] * 300   #LEFT DIAGONAL
rd = [0] * 300   #Right diagonal
cl = [0] * 300   #column check for  row
n = int(input())
board = [[0 for col  in range(n)]for row in range(n)]
ans = solveNQUtil(board,0,n)
if ans==False:print("No sol exist")
else:
    for i in range(n):print(board[i])