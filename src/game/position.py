class Position:
    """A position class that keeps current position
    on a 1-D array index and can convert it to Chess
    notation when needed.
    """

    def __init__(self, index: int):
        self.index = index

    def to_alpha(self, index: int) -> str:
        """Convert from 1-D index to Chess Notation
        For example, Index 0 => A8
        """
        return ""

    def to_index(self, alpha: str) -> int:
        """Convert Chess Notation position to 1-D Index.
        For example, A8 => Index 0
        """
        return 0

    def __str__(self) -> str:
        return self.to_alpha(self.index)
