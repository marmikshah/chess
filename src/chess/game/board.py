from typing import List

from position import Position

from .piece import Piece

FEN_INIT_DEFAULT = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


class Board:
    def __init__(self, fen: str = FEN_INIT_DEFAULT):
        self.board: List[Piece | None] = []

        self.__dead_pieces: List[Piece] = []

        self.decode(fen)

    def decode(self, fen) -> List[str]:
        """Creates a board array from a given Forsyth-Edwards
        Notation (FEN) string.
        """
        print("Creating Board from FEN: ", fen)
        parts = fen.split(" ")
        rows = parts[0].split("/")

        for i, row in enumerate(rows):
            j = 0
            for item in row:
                if item.isdigit():
                    for _ in range(int(item)):
                        self.board[i * 8 + j] = None
                        j += 1
                else:
                    self.board[i * 8 + j] = Piece.from_fen_char(item, i * 8 + j)
                    j += 1

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
        print("Resetting Board with FEN: ", FEN_INIT_DEFAULT)
        self.decode(fen=FEN_INIT_DEFAULT)

    def undo(self):
        """Undo previous move"""
        raise NotImplementedError()
