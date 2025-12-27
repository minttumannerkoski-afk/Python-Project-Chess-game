"""Game controller (v1).

Manages turns, uses rules.validate_move, and applies approved moves to the board.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Optional, Tuple

from board import Board, MoveResult
from rules import validate_move
from utils import is_square, piece_color


@dataclass(frozen=True)
class PlayResult:
    success: bool
    message: str


class Game:
    """High-level game logic for v1 (turns + validated moves)."""

    def __init__(self) -> None:
        self.board = Board()
        self.current_player = "white"  # white starts

    def parse_move(self, text: str) -> Optional[Tuple[str, str]]:
        """Parse user input into (start, end) squares.

        Accepts: "e2 e4" or "e2e4"
        """
        t = text.strip().lower().replace("-", " ").replace(",", " ")
        if not t:
            return None

        parts = t.split()
        if len(parts) == 2:
            start, end = parts
        elif len(parts) == 1 and len(parts[0]) == 4:
            start, end = parts[0][:2], parts[0][2:]
        else:
            return None

        if not (is_square(start) and is_square(end)):
            return None
        return start, end

    def make_move(self, start: str, end: str) -> PlayResult:
        """Attempt to make a move. Returns a user-facing result message."""
        logging.debug("Player %s attempts %s -> %s", self.current_player, start, end)

        verdict = validate_move(self.board, start, end, self.current_player)
        if not verdict.ok:
            return PlayResult(False, verdict.reason)

        applied: MoveResult = self.board.apply_move_unchecked(start, end)
        if not applied.success:
            return PlayResult(False, applied.message)

        if applied.captured:
            return PlayResult(True, f"{self.current_player.capitalize()} captured {applied.captured} on {end}")

        self._swap_turn()
        return PlayResult(True, f"{self.current_player.capitalize()} to move")

    def _swap_turn(self) -> None:
        self.current_player = "black" if self.current_player == "white" else "white"
