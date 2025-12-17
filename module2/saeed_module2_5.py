"""Terminal two-player Tic-Tac-Toe (X / O).

Players alternate entering a number 1-9 corresponding to the board positions:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Usage:
    python module2/saeed_module2_5.py

During play each player is prompted to enter a number for their move.
Invalid or occupied choices are rejected and the player is re-prompted.
"""
from typing import List


WIN_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def display_board(board: List[str]) -> None:
    def p(i):
        return board[i] if board[i] != "" else str(i + 1)

    print(f" {p(0)} | {p(1)} | {p(2)}")
    print("---+---+---")
    print(f" {p(3)} | {p(4)} | {p(5)}")
    print("---+---+---")
    print(f" {p(6)} | {p(7)} | {p(8)}")


def check_winner(board: List[str]) -> str | None:
    for a, b, c in WIN_COMBINATIONS:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board: List[str]) -> bool:
    return all(cell != "" for cell in board)


def get_move(player: str, board: List[str]) -> int:
    while True:
        try:
            raw = input(f"Player {player} - enter position (1-9): ").strip()
            pos = int(raw)
            if pos < 1 or pos > 9:
                print("Please enter a number from 1 to 9.")
                continue
            idx = pos - 1
            if board[idx] != "":
                print("That position is already taken. Choose another.")
                continue
            return idx
        except ValueError:
            print("Invalid input. Enter the number of an empty cell (1-9).")


def play_game() -> None:
    board: List[str] = [""] * 9
    current = "X"

    while True:
        display_board(board)
        move = get_move(current, board)
        board[move] = current

        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            display_board(board)
            print("It's a draw.")
            break

        current = "O" if current == "X" else "X"



    print("Welcome to Tic-Tac-Toe")
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
