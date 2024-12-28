from dataclasses import dataclass
from app.domains.identifiers import UserId, BoardId


class WritePostResult:
    def to_message(self) -> str:
        raise NotImplementedError()


@dataclass
class TitleLengthExceededLimitResult(WritePostResult):
    def to_message(self) -> str:
        return "제목의 글자수가 너무 깁니다."


@dataclass
class AuthorLevelPermissionDeniedResult(WritePostResult):
    def to_message(self) -> str:
        return "게시판에 작성할 권한이 없습니다."


@dataclass
class SuccessfullyWritePostResult(WritePostResult):
    title: str
    content: str
    user_id: UserId
    board_id: BoardId
