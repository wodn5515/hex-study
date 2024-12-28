from typing import Protocol
from app.domains.identifiers import BoardId
from app.domains.boards import Board


class FindBoardPort(Protocol):
    def find_board(self, board_id: BoardId) -> Board:
        raise NotImplementedError()
