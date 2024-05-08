# https://oj.masaischool.com/contest/11933/problems

def solve(board):
    
    

    # Check rows and columns for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '0':
            print(board[i][0])
            exit()
        if board[0][i] == board[1][i] == board[2][i] != '0':
            print(board[0][i])
            exit()

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != '0':
        print(board[0][0])
        exit()
    if board[0][2] == board[1][1] == board[2][0] != '0':
        print(board[0][2])
        exit()

    print("Tie")

    
