from game.board import Board
from overrides import overrides

from .base import BaseEngine


class AlphaBetaTreeSearchEngine(BaseEngine):
    """Implementation of the Alpha Beta tree pruning
    algorithm to select the next best move.
    """

    @overrides
    def get_next_move(self, board: Board): ...
