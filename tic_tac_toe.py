import random

# Main function to start the game
def main():
    print("TIC TAC TOE\n")
    print("1. Player vs Computer")
    print("2. Player vs Player")
    print()
    # Initialize a 3x3 empty game board
    game_board = [
        ['   ','   ','   '],
        ['   ','   ','   '],
        ['   ','   ','   ']
    ]

    # Get user choice for game mode
    while True:
        try:
            user_choice = int(input("Choose any one (1 for PvC, 2 for PvP): ")) 
            if user_choice == 1 or user_choice == 2:
                break # Valid choice
            else:
                print("Invalid choice. Please choose 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Start the game based on user choice
    if user_choice == 1:
        pvc(game_board)
    elif user_choice == 2:
        pvp(game_board)

# Player vs Computer mode logic
def pvc(GB):
    print("\n ---Player vs Computer---\n")

    # Select difficulty level
    print("Difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print()
    level = input_validation('difficulty level')

    # Display the initial empty game board
    display_game_board(GB)
    print()
        
    no_of_turn = 1 # Track number of turns (max 9)

    # Main game loop
    while no_of_turn < 10:
        # Determine whose turn it is based on the turn number

        # Player's turn on odd turns
        if no_of_turn % 2 == 1:
            print("--Your turn--\n")
            # Input validation loop for row and column selection
            while True:
                row = input_validation("row")
                column = input_validation("column")
                if GB[row - 1][column - 1] != '   ':
                    print("This cell is already occupied. Choose another one.")
                    continue
                else:
                    break
            GB[row - 1][column - 1] = ' O ' 

        # Computer's turn on even turns
        else:
            print("--Computer's turn--\n")
            if level == 1:
                computer_move_easy(GB)
            elif level == 2:
                computer_move_medium(GB)
            elif level == 3:
                computer_move_hard(GB)

        # Display the updated game board
        display_game_board(GB)
        print()

        winner = check_winner(GB)
        if winner:
            print(f"{'Player' if winner == ' O ' else 'Computer'} wins!")
            return

        no_of_turn += 1

    print("It's a draw!")

# Player vs Player mode logic
def pvp(GB):
    print("\n ---Player vs Player---\n")

    # Display the initial empty game board
    display_game_board(GB)
    print()

    no_of_turn = 1 # Track the number of turns 
    while no_of_turn < 10:
        # Determine whose turn it is based on the turn number
        if no_of_turn % 2 == 1:
            print("--Player 1's turn--")
        else:
            print("--Player 2's turn--")

        # Input validation loop for row and column selection
        while True:
            row = input_validation("row")
            column = input_validation("column")
            print()
            if GB[row - 1][column - 1] != '   ':
                print("This cell is already occupied. Choose another one.")
                continue
            else:
                break

        # Assign 'O' to Player 1 and 'X' to Player 2 based on the turn number
        if no_of_turn % 2 == 1:
            GB [row - 1] [column - 1] = ' O '
        else:
            GB [row - 1] [column - 1] = ' X '

        # Display the updated game board
        display_game_board(GB)
        print()

           # Check for a winner after each move
        winner = check_winner(GB)
        if winner:
            print(f"{'Player 1' if winner == ' O ' else 'Player 2'} wins!")
            return

        no_of_turn += 1 # Increment the turn counter

    # If no winner is found after 9 turns, it's a draw
    print("It's a draw!")

# Function to validate input for row/column/difficulty level selection
def input_validation(value_type):
   while True: 
        try:
            user_input = int(input(f"Choose {value_type}(1-3): "))
            if 1 <= user_input <= 3:
                return user_input # Return valid input
        except ValueError:
            print("Invalid input. Please enter a number.")
            
# Function to check for a winner in the game board
def check_winner(GB):
    # Check rows and columns for a winner
    for i in range(3):
        if GB[i][0] == GB[i][1] == GB[i][2] != '   ':
            return GB[i][0]
        if GB[0][i] == GB[1][i] == GB[2][i] != '   ':
            return GB[0][i]

    # Check diagonals for a winner
    if GB[0][0] == GB[1][1] == GB[2][2] != '   ':
        return GB[0][0]
    if GB[0][2] == GB[1][1] == GB[2][0] != '   ':
        return GB[0][2]

    return None # No winner yet

def display_game_board(GB):
    for i in range(3):
        print(f"{'|'.join(GB[i])}")
        if i!= 2:
            print("---|---|---")

def computer_move_easy(GB):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if GB[i][j] == '   ':
                empty_cells.append((i, j))

    if empty_cells:
        row, column = random.choice(empty_cells)
        GB[row][column] = ' X '

def computer_move_medium(GB):
    # Check if computer can win
    for i in range(3):
        for j in range(3):
            if GB[i][j] == '   ':
                GB[i][j] = ' X '
                if check_winner(GB) == ' X ':
                    return
                GB[i][j] = '   '

    # Block if player is about to win
    for i in range(3):
        for j in range(3):
            if GB[i][j] == '   ':
                GB[i][j] = ' O '
                if check_winner(GB) == ' O ':
                    GB[i][j] = ' X '
                    return
                GB[i][j] = '   '

    # Otherwise, random move
    computer_move_easy(GB)


def computer_move_hard(GB):
    # Code to be implemented soon
    ...
     
if __name__ == "__main__":
    main()
