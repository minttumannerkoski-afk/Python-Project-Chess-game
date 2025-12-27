"""CLI entry point for Chess (v1)."""

from __future__ import annotations

import argparse
import logging

from game import Game


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Chess CLI (v1): turn-based play with basic move validation (no check/checkmate)."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging."
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s"
    )

    game = Game()
    game.board.display()
    print("Type moves like: e2 e4  (or e2e4). Type 'quit' to exit.\n")
    print("White to move")

    while True:
        text = input("> ").strip()
        if text.lower() in {"quit", "exit"}:
            break

        parsed = game.parse_move(text)
        if not parsed:
            print("Invalid input. Example: e2 e4")
            continue

        start, end = parsed
        result = game.make_move(start, end)
        print(result.message)
        if result.success:
            game.board.display()


if __name__ == "__main__":
    main()
