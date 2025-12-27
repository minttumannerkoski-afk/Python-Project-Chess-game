"""Move validation rules (v1).

v1 validates piece movement, captures, blocking, and pawn basics.
v1 does NOT handle: check/checkmate, castling, en passant, promotion.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

from utils import to_coords, to_square, piece_color, piece_type


@dataclass(frozen=True)
class Validation:
    ok: bool
    reason: str


def _delta(start: str, end: str) -> Tuple[int, int]:
    sx, sy = to_coords(start)
    ex, ey = to_coords(end)
    return ex - sx, ey - sy


def _sign(x: int) -> int:
    return (x > 0) - (x < 0)


def _path_clear(board, start: str, end: str) -> bool:
    """Return True if all intermediate squares between start and end are empty."""
    dx, dy = _delta(start, end)
    step_x, step_y = _sign(dx), _sign(dy)

    sx, sy = to_coords(start)
    ex, ey = to_coords(end)

    cx, cy = sx + step_x, sy + step_y
    while (cx, cy) != (ex, ey):
        sq = to_square(cx, cy)
        if board.occupied(sq):
            return False
        cx += step_x
        cy += step_y
    return True


def validate_move(board, start: str, end: str, player: str) -> Validation:
    """Validate a move for the current player."""
    piece = board.get(start)
    if piece is None:
        return Validation(False, f"No piece at {start}")

    if piece_color(piece) != player:
        return Validation(False, f"Not your piece at {start}")

    if start == end:
        return Validation(False, "Start and end are the same square")

    target = board.get(end)
    if target is not None and piece_color(target) == player:
        return Validation(False, "Destination occupied by your own piece")

    ptype = piece_type(piece)
    if ptype is None:
        return Validation(False, "Unknown piece type")

    if ptype == "p":
        return _validate_pawn(board, start, end, piece, target)
    if ptype == "r":
        return _validate_rook(board, start, end)
    if ptype == "n":
        return _validate_knight(start, end)
    if ptype == "b":
        return _validate_bishop(board, start, end)
    if ptype == "q":
        return _validate_queen(board, start, end)
    if ptype == "k":
        return _validate_king(start, end)

    return Validation(False, "Unsupported piece in v1")


def _validate_rook(board, start: str, end: str) -> Validation:
    dx, dy = _delta(start, end)
    if dx != 0 and dy != 0:
        return Validation(False, "Rook moves in straight lines only")
    if not _path_clear(board, start, end):
        return Validation(False, "Path is blocked")
    return Validation(True, "OK")


def _validate_bishop(board, start: str, end: str) -> Validation:
    dx, dy = _delta(start, end)
    if abs(dx) != abs(dy):
        return Validation(False, "Bishop moves diagonally only")
    if not _path_clear(board, start, end):
        return Validation(False, "Path is blocked")
    return Validation(True, "OK")


def _validate_queen(board, start: str, end: str) -> Validation:
    dx, dy = _delta(start, end)
    straight = (dx == 0 or dy == 0)
    diagonal = (abs(dx) == abs(dy))
    if not (straight or diagonal):
        return Validation(False, "Queen moves straight or diagonally")
    if not _path_clear(board, start, end):
        return Validation(False, "Path is blocked")
    return Validation(True, "OK")


def _validate_knight(start: str, end: str) -> Validation:
    dx, dy = _delta(start, end)
    if (abs(dx), abs(dy)) not in {(1, 2), (2, 1)}:
        return Validation(False, "Knight moves in an L-shape (2+1)")
    return Validation(True, "OK")


def _validate_king(start: str, end: str) -> Validation:
    dx, dy = _delta(start, end)
    if max(abs(dx), abs(dy)) != 1:
        return Validation(False, "King moves one square only (no castling in v1)")
    return Validation(True, "OK")


def _validate_pawn(board, start: str, end: str, piece: str, target: Optional[str]) -> Validation:
    """Pawn rules (v1): forward moves, double from start rank, diagonal capture."""
    dx, dy = _delta(start, end)
    color = piece_color(piece)
    if color is None:
        return Validation(False, "Invalid pawn")

    # Direction: white increases rank (dy +), black decreases rank (dy -)
    forward = 1 if color == "white" else -1

    # Single step forward
    if dx == 0 and dy == forward:
        if target is not None:
            return Validation(False, "Pawn cannot move forward into an occupied square")
        return Validation(True, "OK")

    # Double step from start rank
    start_rank = start[1]
    is_starting = (color == "white" and start_rank == "2") or (color == "black" and start_rank == "7")
    if dx == 0 and dy == 2 * forward and is_starting:
        if target is not None:
            return Validation(False, "Pawn cannot move forward into an occupied square")
        # Intermediate square must be empty
        sx, sy = to_coords(start)
        mid_sq = to_square(sx, sy + forward)
        if board.occupied(mid_sq):
            return Validation(False, "Pawn double-step is blocked")
        return Validation(True, "OK")

    # Diagonal capture
    if abs(dx) == 1 and dy == forward:
        if target is None:
            return Validation(False, "Pawn captures diagonally only (no en passant in v1)")
        return Validation(True, "OK")

    return Validation(False, "Illegal pawn move")
