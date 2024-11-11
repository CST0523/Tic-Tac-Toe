import random

# Display instructions
def instruction():
    print("Tic-Tac-Toe Game")
    print("The rules of Tic-Tac-Toe: The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.\n")

# Ask the player to choose a character and decide who goes first
def select():
    select_first = ""
    while select_first not in ["Y", "N"]:
        select_first = input("Do you want to go first? (Y/N) ").upper()
    
    if select_first == "Y":
        human = ""
        while human not in ["X", "O"]:
            human = input("Which character do you want to be? (X/O) ").upper()
        comp = "O" if human == "X" else "X"
        print(f"Your character is '{human}', computer is '{comp}'.")
        turn = human
    else:
        human, comp = "O", "X"
        print("You are 'O', and the computer is 'X'.")
        turn = comp
    
    return human, comp, turn

# Initialize an empty board
def emptyboard():
    return [" "] * 9

# Draw the board and initial position numbers
def drawboard(board, show_index=False):
    if show_index:
        # Display board with position numbers for reference
        print("   0 | 1 | 2 ")
        print("  -----------")
        print("   3 | 4 | 5 ")
        print("  -----------")
        print("   6 | 7 | 8 ")
    else:
        # Display the current board with player moves
        print(f"   {board[0]} | {board[1]} | {board[2]}")
        print("  -----------")
        print(f"   {board[3]} | {board[4]} | {board[5]}")
        print("  -----------")
        print(f"   {board[6]} | {board[7]} | {board[8]}")

# Handle player's move
def humanchoice(board, human):
    move = -1
    while move not in range(9) or board[move] != " ":
        try:
            move = int(input("Choose a position (0-8): "))
            if board[move] != " ":
                print("Position already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 8.")
    board[move] = human

# Handle computer's move
def compchoice(board, comp):
    move = random.choice([i for i in range(9) if board[i] == " "])
    board[move] = comp
    print(f"Computer chose position {move}")

# Check for a winner or tie
def checkwinner(board, human, comp):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]
    if " " not in board:
        return "Tie"
    return None

# Display result and ask if the player wants to play again
def result(winner, human, comp):
    if winner == human:
        print("Congratulations, you won!")
    elif winner == comp:
        print("Sorry, the computer won.")
    else:
        print("It's a tie!")
    return input("Do you want to play again? (Y/N): ").upper() == "Y"

# Main game function
def main():
    instruction()
    play_again = True
    while play_again:
        human, comp, turn = select()  # Get initial choices and who goes first
        board = emptyboard()
        game_over = False

        # Display initial board with indices
        print("\nBoard positions:")
        drawboard(board, show_index=True)
        
        while not game_over:
            drawboard(board)  # Show current board with moves only
            if turn == human:
                humanchoice(board, human)
            else:
                compchoice(board, comp)
            
            winner = checkwinner(board, human, comp)
            if winner:
                drawboard(board)
                play_again = result(winner, human, comp)
                game_over = True
            turn = comp if turn == human else human  # Switch turns

if __name__ == "__main__":
    main()
