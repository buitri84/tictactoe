import copy
import os

# Declare set of winning states
winning = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]

# Declare a universal weight variable to reward fast win choice
weight = 0.9

# This function checks if a move is legal and updates the board, returning True. Returns False if move is not legal
def move(board, pos, player):
    if board[pos] != 0:
        return False
    else:
        if player == 1:
            board[pos] = "X"
        elif player == -1:
            board[pos] = "Y"
        return True

# This function checks the state of the game and return the score (100 if player 1 wins, -100 if player -1 wins, and 0 if it is a draw)
# an incomplete game returns False, while completed game returns True
def gameover(board):
    # Create 2 vectors for state of players and populate them
    player_x = set()
    player_o = set()
    for i in range(9):
        if board[i] == "X":
            player_x.add(i)
        elif board[i] == "Y":
            player_o.add(i)
    # print(player_x)
    # print(player_o)
    # Check if any player has winning combination
    for i in winning:
        if i <= player_x:
            return True, 100
        elif i <= player_o:
            return True, -100
    # If not, then it's either just an incomplete game or a draw
    for i in board:
        if i == 0:
            return False, 0
    return True, 0

# Minimax function: recursively calls itself to obtain the score for every possible move. Returns max or min score depending on player
# Also: returns what is supposedly the best move. Each recursive call, the function updates the list of moves. It matches the move with
# the score (by using the index of the max or min score) hence returns the optimal move.
def minimax(board, player):
    state, score = gameover(board)
    if state == True:
        return score, -1  # In base case, there is no best move so just return -1
    else:
        # Obtain all possible moves
        moves = []
        for i in range(9):
            if board[i] == 0:
                moves.append(i)
        # Calculate values (ie. the array of scores) for all possible moves
        values = []
        for m in moves:
            new_board = copy.deepcopy(board)
            mov = move(new_board, m, player)
            v, d_m = minimax(new_board, -1*player)
            values.append(weight*v)
        # Maximize value if player = 1, minimize if player = -1
        if player == 1:
            value = max(values)
            best_move = moves[values.index(max(values))]
        elif player == -1:
            value = min(values)
            best_move = moves[values.index(min(values))]
        # print("Values: ", values)
        # print("Moves: ", moves)
        return value, best_move

def main():
    # Declare board. Note: Actually I just need an array, no need for complicated structure
    board = []
    for i in range(9):
        board.append(0)
    print("---Tic Tac Toe game. As human, you are player X. The bot is player Y.---")
    print("The board is just a grid of 9 initially empty squares, with position indicated as followed: ")
    print("[0 1 2\n 3 4 5\n 6 7 8]")
    print("Simply enter the number corresponding to the location you want to play when prompted")
    # Set flag for starting player
    flag = 1
    # Loop to keep getting input where to play
    while True:
        state, score = gameover(board)
        # print(state, score)
        if state == True:
            if score == 100:
                print("Player X wins")
                break
            elif score == -100:
                print("Player Y wins")
                break
            elif score == 0:
                print("Draw!!!")
                break
        # human player
        if flag == 1:
            pos = int(input("Enter the position where you want to make a move (0-8): "))
            if pos > 8 or pos < 0:
                print("Only input a number between 0 and 8 inclusive")
            else:
                mov = move(board, pos, flag)
                if mov == True:    # if move has succeded, switch player, otherwise same player tries again
                    flag = -1*flag
                    os.system('cls||clear')
        # computer player
        elif flag == -1:
            value, best_move = minimax(board, flag)
            mov = move(board, best_move, flag)
            if mov == True:
                flag = -1* flag
            # print("Minimax value: ", value)
            print("Minimax (bot) has chosen to move: ", best_move)
        print(board[0:3])
        print(board[3:6])
        print(board[6:9])

if __name__ == "__main__":
    main()
