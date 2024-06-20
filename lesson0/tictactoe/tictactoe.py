"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    round=9

    for i in board:
        for j in range(len(i)):
            if i[j] == EMPTY:
                round -= 1

    if round%2==0 or round==0:
        turn = X

    else:
        turn = O

    return turn



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibilities=set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibilities.add((i,j))

    return possibilities


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    if action not in actions(board):
        raise ValueError
    
    board_copy=[[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    for i in range(3):
        for j in range(3):
            board_copy[i][j] = board[i][j]
    
    x,y = action

    board_copy[x][y] = player(board)

    return board_copy



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check horizontals
    diagonal = []
    diagonaltwo = []

    for i in range(3):
        column = []
        row = []
        
        if (len(diagonal) == 0 or diagonal[0] == board[i][i]) and board[i][i] != EMPTY:
            diagonal.append(board[i][i])

        if (len(diagonaltwo) == 0 or diagonaltwo[0] == board[i][2-i]) and board[i][2-i] != EMPTY:
            diagonaltwo.append(board[i][2-i])

        for j in range(3):
            if (len(column) == 0 or column[0] == board[j][i]) and board[j][i] != EMPTY:
                column.append(board[j][i])

            if (len(row) == 0 or row[0] == board[i][j]) and board[i][j] != EMPTY:
                row.append(board[i][j])

        if len(column) == 3:
            return column[0]
        
        if len(row) == 3:
            return row[0]
    
    if len(diagonal) == 3:
        return diagonal[0]
    
    if len(diagonaltwo) == 3:
        return diagonaltwo[0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or len(actions(board))==0:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == O:
        return -1
    
    if winner(board) == X:
        return 1
    
    return 0

def maxValue(board):
    v = -math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v=max(v, minValue(result(board,action))) 
    
    return v

def minValue(board):
    v = math.inf
    
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v=min(v,maxValue(result(board,action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    posActions = list(actions(board))

    if terminal(board):
        return None

    if len(posActions) == 9:
        return (1,1)

    if player(board) == X:
        minValues = []

        for i in posActions:
            minValues.append(minValue(result(board,i)))
        
        return posActions[minValues.index(max(minValues))]

    if player(board) == O:
        maxValues = []
        
        for i in posActions:
            maxValues.append(maxValue(result(board,i)))
        
        return posActions[maxValues.index(min(maxValues))]