import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

def evaluate(board):
  
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return 10 if row[0] == 'X' else -10

 
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return 10 if board[0][col] == 'X' else -10

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return 10 if board[0][2] == 'X' else -10

    return 0


def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

  
    if not is_moves_left(board):
        return 0

   
    if is_max:
        best = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best

  
    else:
        best = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best


def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move


def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human = 'O'
    ai = 'X'
    current_player = human

    while True:
        print_board(board)

        if current_player == human:
            while True:
                move = input("Enter your move (row col) where row and col are between 0 and 2: ")
                try:
                    row, col = map(int, move.split())
                    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                        board[row][col] = human
                        current_player = ai
                        break
                    else:
                        print("Invalid move! The cell is either occupied or out of bounds. Try again.")
                except ValueError:
                    print("Invalid input! Please enter two numbers separated by a space, like '1 2'.")
        else:
            print("AI is making a move...")
            row, col = find_best_move(board)
            board[row][col] = ai
            current_player = human

     
        score = evaluate(board)
        if score == 10:
            print_board(board)
            print("AI wins!")
            break
        elif score == -10:
            print_board(board)
            print("You win!")
            break
        elif not is_moves_left(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
