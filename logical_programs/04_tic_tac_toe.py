def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    moves = 0

    while True:
        print_board(board)
        row, col = map(int, input(f"player {player}, enter row and column (x,y)").split())
        
        if board[row][col] == " ":
            board[row][col] = player
            moves += 1

            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            
            if moves == 9:
                print_board(board)
                print("It's a draw!")
                break

            player = "O" if player == "X" else "X"
        else:
            print("Cell already occupied! Try again.")

tic_tac_toe()
