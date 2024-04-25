from typing import List

from piece import Piece
from position import Position


class Board:
    def __init__(self, fen: str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.board: List[Piece | None] = []

        self.__dead_pieces: List[Piece] = []

    def decode(self, fen) -> List[str]:
        """Creates a board array from a given Forsyth-Edwards
        Notation (FEN) string.
        """
        return []

    def encode(self) -> str:
        """Encode's current board array into a Forsyth-Edwards
        Notation (FEN) returned as a string.
        """
        return ""

    def move(self, piece: Piece, position: Position) -> int:
        """Make a move on the board and return an int
        indicating the score of this move. It will be
        non-zero when a piece is killed.

        Killed Pieces can be viewed from `self.__dead_pieces`

        """
        index = position.index
        score = 0
        if self.board[index] is not None:
            score = self.board[index].type.value
            self.__dead_pieces.append(self.board[index])

        self.board[position.to_index(position.index)] = piece

        return score

    def reset(self):
        """Reset to starting position"""
        ...

    def undo(self):
        """Undo previous move"""
        raise NotImplementedError()
