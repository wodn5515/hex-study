from typing import Protocol
from myapp.domains.identifiers import BoardId
from myapp.domains.boards import Board


class FindBoardPort(Protocol):
    def find_board(self, board_id: BoardId) -> Board:
        raise NotImplementedError()
