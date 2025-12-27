"""Utility helpers for coordinates and piece properties."""

from __future__ import annotations

import re
from typing import Tuple, Optional

FILES = "abcdefgh"
RANKS = "12345678"

SQUARE_RE = re.compile(r"^[a-h][1-8]$")


def is_square(square: str) -> bool:
    """Return True if square is in algebraic form a1..h8."""
    return bool(SQUARE_RE.match(square))


def to_coords(square: str) -> Tuple[int, int]:
    """Convert 'a1'..'h8' into (file_index, rank_index) where 0..7 each."""
    file_char = square[0]
    rank_char = square[1]
    return FILES.index(file_char), RANKS.index(rank_char)


def to_square(file_idx: int, rank_idx: int) -> str:
    """Convert (file_index, rank_index) back into 'a1'..'h8'."""
    return f"{FILES[file_idx]}{RANKS[rank_idx]}"


def piece_color(piece: str) -> Optional[str]:
    """Return 'white' if uppercase, 'black' if lowercase, None if empty/invalid."""
    if not piece or len(piece) != 1:
        return None
    if piece.isupper():
        return "white"
    if piece.islower():
        return "black"
    return None


def piece_type(piece: str) -> Optional[str]:
    """Return normalized piece type letter in lowercase: p,r,n,b,q,k."""
    if not piece or len(piece) != 1:
        return None
    letter = piece.lower()
    return letter if letter in {"p", "r", "n", "b", "q", "k"} else None
