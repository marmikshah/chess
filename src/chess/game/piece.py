from dataclasses import dataclass
from enum import IntEnum

from position import Position


class Color(IntEnum):
    """Binary mapping for the Color of
    the Chess Piece.
    The same mapping can also be used for
    player's color.
    """

    WHITE = 0b0000
    BLACK = 0b0001


class Type(IntEnum):
    """A Binary mapping for the type
    of Chess Piece
    """

    PAWN = 0b0010
    KNIGHT = 0b0100
    BISHOP = 0b0110
    ROOK = 0b1000
    QUEEN = 0b1010
    KING = 0b1100

    @staticmethod
    def from_fen_char(char: str):
        """Convert `char` to Type"""

        piece_type = {
            "p": Type.PAWN,
            "n": Type.KNIGHT,
            "b": Type.BISHOP,
            "r": Type.ROOK,
            "q": Type.QUEEN,
            "k": Type.KING,
        }

        return piece_type[char.lower()]


@dataclass
class Piece:
    """Piece metadata class."""

    position: Position
    color: Color
    type: Type

    def __str__(self):
        return f"{self.color.name} {self.type.name} @ {self.position}"

    @staticmethod
    def from_fen_char(char: str, index: int):
        """Converts a FEN character to a Piece instance."""
        _type = Type.from_fen_char(char)
        _color = Color.WHITE if char.isupper() else Color.BLACK
        _position = Position(index)

        return Piece(_position, _color, _type)
