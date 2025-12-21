import random

# Define the possible moves
moves = ["UP", "RIGHT", "DOWN", "LEFT"]

# Function to draw the game board
def draw_board(current_grid):
    print("  ---+---+---+---") # Adjusted for 4x4
    for row in current_grid:
        # Convert all items in the row to strings before joining
        print("| " + " | ".join(str(item) for item in row) + " |")
        print("  ---+---+---+---")

# Function to display the board with the player's position
def display_board(game_grid, player_pos):
    # Create a temporary grid to mark the player's position for display
    display_grid = [row[:] for row in game_grid] # Make a copy
    px, py = player_pos
    display_grid[px][py] = 'P' # Mark player's position with 'P'

    draw_board(display_grid)
    print(f"\nYou are currently at: ({px}, {py})")

# Function to check if a move is valid
def is_valid_move(board_dims, current_pos, move_direction):
    directions = {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}
    dx, dy = directions[move_direction]
    cx, cy = current_pos
    new_x, new_y = cx + dx, cy + dy
    
    # Check if the new position is within board boundaries
    return 0 <= new_x < board_dims[0] and 0 <= new_y < board_dims[1]

# Function to calculate the new position after a move
def calculate_new_position(current_pos, move_direction):
    directions = {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}
    dx, dy = directions[move_direction]
    cx, cy = current_pos
    return (cx + dx, cy + dy)

# Main game loop
def olla_game():
    board_rows, board_cols = 4, 4
    # Initialize a 4x4 empty game board
    game_board = [[' ' for _ in range(board_cols)] for _ in range(board_rows)]
    player_pos = (0, 0) # Player starts at top-left corner

    print("Welcome to the Olla Game!")
    print("Move 'P' around the 4x4 board. Reach (3,3) to win!")

    while True:
        display_board(game_board, player_pos)
        print("\nChoose your move:")
        print("1. UP")
        print("2. RIGHT")
        print("3. DOWN")
        print("4. LEFT")

        choice = input("Enter the number of your move: ")

        move_direction = None
        if choice == "1":
            move_direction = "UP"
        elif choice == "2":
            move_direction = "RIGHT"
        elif choice == "3":
            move_direction = "DOWN"
        elif choice == "4":
            move_direction = "LEFT"
        else:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if is_valid_move((board_rows, board_cols), player_pos, move_direction):
            player_pos = calculate_new_position(player_pos, move_direction)
            # Check for win condition (e.g., reaching a specific target cell)
            if player_pos == (board_rows - 1, board_cols - 1): # Reaching bottom-right corner
                display_board(game_board, player_pos)
                print("\nCongratulations! You reached the target (3,3) and won!")
                break
        else:
            print("Invalid move: You cannot move off the board. Try again.")

# Start the game
olla_game()