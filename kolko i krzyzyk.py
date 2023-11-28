board=  ["-","-","-",
           "-","-","-",
           "-","-","-",]
gracz= "X"
zwyciezca= None
Gamerunning=True


def printBoard(board):
    print(board[0]+ " | " + board[1] + " | " +board[2])
    print(board[3]+ " | " + board[4] + " | " +board[5])
    print(board[6]+ " | " + board[7] + " | " +board[8])
    
    

def playerInput(board):
    inp = input("wybierz numer od 1 do 9")
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = gracz
    else:
        print("to pole jest juz zajete")


def trojka_poziomo(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def trojka_po_skosie(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[6] == board[4] == board[2] and board[6] != "-":
        winner = board[6]
        return True
    
def trojka_pionowo(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[3] != "-":
        winner = board[2]
        return True    






while Gamerunning:
    printBoard(board) 
    playerInput(board)