import random

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

gameOver = True
player1 = ''
player2 = ''
turn = ''
numturn = 0

def tictactoe(p1:str,p2:str):
    global gameOver
    global turn
    global numturn
    global player1
    global player2
    player1 = p1
    player2 = p2
    if gameOver:
        global board
        print(render(board))
        num = random.randint(1,2)
        if num == 1:
            turn = player1
            numturn = 1
            print("{} Turn! | [O]".format(turn))
        elif num == 2:
            turn = player2
            numturn = 2
            print("{} Turn! | [X]".format(turn))
        gameOver = False

def place(num):
    global gameOver
    global turn
    global numturn
    global player1
    global player2
    if not gameOver:
        global board
        if num >= 1 and num <= 3:
            if board[0][num-1] != 0:
                print(render(board))
                print("Can't place.")
                return
            else:
                board[0][num-1] = numturn
        if num >= 4 and num <= 6:
            if board[1][num-4] != 0:
                print(render(board))
                print("Can't place.")
                return
            else:
                board[1][num-4] = numturn
        if num >= 7 and num <= 9:
            if board[2][num-7] != 0:
                print(render(board))
                print("Can't place.")
                return
            else:
                board[2][num-7] = numturn
        win,winpeople = windetect(board)
        tie = tiedetect(board)
        if tie:
            print(render(board))
            print("Game Over!")
            print("Tie!")
            return True
        if win:
            print(render(board))
            print("Game Over!")
            print("{} Win!".format(winpeople))
            gameOver = True
            return True
        print(render(board))
        if turn == player1:
            turn = player2
            numturn = 2
            print("{} Turn! | [X]".format(turn))
        elif turn == player2:
            turn = player1
            numturn = 1
            print("{} Turn! | [O]".format(turn))
        return False
    else:
        print("Please start the game")

def tiedetect(board):
    tie = []
    if board != [[0,0,0],[0,0,0],[0,0,0]]:
        for x in board:
            for y in x:
                if y == 0:
                    return False
    return True

def windetect(board):
    j = 0
    global numturn
    global turn
    #check |
    for i in range(3):
        if board[i][j] == numturn and board[i][j+1] == numturn and board[i][j+2] == numturn:
            return True,turn
    
    #check -
    for i in range(3):
        if board[j][i] == numturn and board[j+1][i] == numturn and board[j+2][i] == numturn:
            return True,turn

    #check /
    if board[0][2] == numturn and board[1][1] == numturn and board[2][0] == numturn:
        return True,turn
    
    #check \
    if board[0][0] == numturn and board[1][1] == numturn and board[2][2] == numturn:
        return True,turn
    
    return False,''

def render(board):
    line = ''
    for i in board:
        for index,y in enumerate(i):
            if y == 0:
                line += ('#' + ' ')
            elif y == 1:
                line += ('O'+' ')
            elif y == 2:
                line += ("X"+ ' ')
            
            #stop print in the last
            if index < 2:
                line += ('| ')
        line += '\n'
        line += "---------\n"
    return line

if __name__ == '__main__':
    print("\n\n")
    print("Tictactoe Game!\n")
    tictactoe('Bob','Alice')
    while True:
        try:
            inp1 = int(input("Select 1- 9 : "))
            print("--------------------------\n")
            gameover = place(inp1)
            if gameover:
                break
        except ValueError:
            print("Stopped")
            break