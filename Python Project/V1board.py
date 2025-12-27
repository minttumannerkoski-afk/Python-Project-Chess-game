"""Board module.

Stores piece positions and applies moves.
v1: board has no rule logic; rules live in rules.py.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Tuple

from pieces import INITIAL_PIECES
from utils import piece_color


@dataclass(frozen=True)
class MoveResult:
    """Result of attempting to apply a move on the board."""
    success: bool
    message: str
    captured: Optional[str] = None


class Board:
    """Represents a chessboard using a dict mapping squares to piece symbols."""

    def __init__(self) -> None:
        self._pos: Dict[str, str] = {}
        self.setup_board()

    def setup_board(self) -> None:
        """Initialize the board to the standard starting position."""
        self._pos = INITIAL_PIECES.copy()

    def get(self, square: str) -> Optional[str]:
        """Get piece at square, or None."""
        return self._pos.get(square)

    def occupied(self, square: str) -> bool:
        """Return True if square has a piece."""
        return square in self._pos

    def is_enemy(self, from_piece: str, target_square: str) -> bool:
        """Return True if target square contains an enemy piece."""
        target_piece = self.get(target_square)
        if target_piece is None:
            return False
        return piece_color(from_piece) != piece_color(target_piece)

    def apply_move_unchecked(self, start: str, end: str) -> MoveResult:
        """Apply a move without validation (used after rules approve).

        Captures any piece on the destination.
        """
        piece = self.get(start)
        if piece is None:
            return MoveResult(False, f"No piece at {start}")

        captured = self.get(end)
        self._pos[end] = piece
        del self._pos[start]
        return MoveResult(True, f"Moved {start} -> {end}", captured=captured)

    def display(self) -> None:
        """Print the board to the terminal."""
        print("\n  a b c d e f g h")
        print("  ---------------")
        for row in range(8, 0, -1):
            print(row, end="| ")
            for col in "abcdefgh":
                sq = f"{col}{row}"
                piece = self._pos.get(sq, ".")
                print(piece, end=" ")
            print(f"|{row}")
        print("  ---------------")
        print("  a b c d e f g h\n")
