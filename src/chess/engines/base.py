from abc import ABC, abstractmethod

from game.board import Board
from game.piece import Color


class BaseEngine(ABC):
    """Abstract class for the Chess Engines"""

    def __init__(self, color: Color) -> None:
        super().__init__()
        self.color = color

    @abstractmethod
    def play_next_move(self, board: Board):
        """Make the next move directly on the `board`
        instance.
        """
        raise NotImplementedError()
