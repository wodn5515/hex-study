from dataclasses import dataclass
from app.community.domains.identifiers import UserId, BoardId, PostId
from app.community.domains.common import Level
from app.community.domains.boards import Board
from app.community.domains.results.posts import WritePostResult

TITLE_LENGTH_LIMIT = 50


@dataclass
class Post:
    id: PostId
    title: str
    content: str
    author_id: UserId
    board_id: BoardId

@dataclass
class Author:
    id: UserId
    level: Level

    def write_post(self, title: str, content: str, board: Board) -> WritePostResult:
        pass

    def _title_length_exceeded_limit(self, title: str):
        return len(title) > TITLE_LENGTH_LIMIT
    
    def _author_has_permission_level(self, board_level: Level):
        return self.level >= board_level
