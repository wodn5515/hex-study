from dataclasses import dataclass
from typing import Optional
from myapp.domains.identifiers import UserId, BoardId, PostId
from myapp.domains.common import Level, Dt
from myapp.domains.boards import Board
from myapp.domains.results.posts import (
    WritePostResult,
    TitleLengthExceededLimitResult,
    AuthorLevelPermissionDeniedResult,
    SuccessfullyWritePostResult
)

TITLE_LENGTH_LIMIT = 50


@dataclass
class Post:
    id: Optional[PostId] = None
    created_at: Optional[Dt] = None
    updated_at: Optional[Dt] = None
    title: str
    content: str
    author_id: UserId
    board_id: BoardId

@dataclass
class Author:
    id: UserId
    level: Level

    def write_post(self, title: str, content: str, board: Board) -> WritePostResult:
        if self._title_length_exceeded_limit(title=title):
            return TitleLengthExceededLimitResult()
        
        if not self._author_has_permission_level(board_level=board.level):
            return AuthorLevelPermissionDeniedResult()
        
        return SuccessfullyWritePostResult(title=title, content=content, user_id=self.id, board_id=board.id)

    def _title_length_exceeded_limit(self, title: str):
        return len(title) > TITLE_LENGTH_LIMIT
    
    def _author_has_permission_level(self, board_level: Level):
        return self.level >= board_level
