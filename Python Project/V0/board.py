"""Board module.

Provides the Board class, which stores piece positions and prints the board.
Version 0: supports manual piece moves without validating chess rules.
"""

'''class Board:
  def __init__(self):
      self.grid = [[None for _ in range(8)] for _ in range(8)]

  def is_empty(self, row, col):
     if 0 <= row <= 8 and 0 <= col <= 8:
        return self.grid[row][col] is None
     return False 
  
  def place_position(self, piece, row, col):
    self.grid[row][col] = piece
    piece.position = (row, col)
     
    #board = [[Board(col, row) for row in range(1, 9)] for col in range(1, 9)]'''

from pieces import INITIAL_PIECES

class Board:
    def __init__(self):
        self.board = {}
        self.setup_board()

    def setup_board(self):
        """
        Initialize the chess board with pieces
        in their standard starting positions.
        """
        self.board = INITIAL_PIECES.copy()

    def move_piece(self, start, end):
        """
        Move a piece from start to end position
        without any validation.
        """
        if start not in self.board:
            print(f"No piece at {start}")
            return

        self.board[end] = self.board[start]
        del self.board[start]

    def display(self):
        """
        Display the board in the terminal.
        """
        print("\n  a b c d e f g h")
        print("  ---------------")

        for row in range(8, 0, -1):
            print(row, end="| ")
            for col in "abcdefgh":
                position = f"{col}{row}"
                piece = self.board.get(position, ".")
                print(piece, end=" ")
            print(f"|{row}")

        print("  ---------------")
        print("  a b c d e f g h\n")

