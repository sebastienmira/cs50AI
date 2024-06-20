from tictactoe import player, actions, result, winner, terminal, utility, minimax
X = "X"
O = "O"
EMPTY = None

board=[[X, EMPTY, X],
        [EMPTY, EMPTY, EMPTY],
        [X, X, X]]

#print(player(board))
#print(actions(board))
#print(result(board,(2,1)))
print(winner(board))
#print(terminal(board))
#print(utility(board))
#print(minimax(board))
