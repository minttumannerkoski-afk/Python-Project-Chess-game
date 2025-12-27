"""CLI entry point for the chess project (v0).

Allows users to move pieces by entering coordinates like: e2 e4.
No chess-rule validation is performed in v0.
"""


from board import Board
from rook import Rook

def main():
    board = Board()
    board.display()

    while True:
        move = input("Enter move (e2 e4): ")
        if move == "quit":
            break
        start, end = move.split()
        board.move_piece(start, end)
        board.display()

if __name__ == "__main__":
    main()
