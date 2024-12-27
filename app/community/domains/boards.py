from dataclasses import dataclass
from app.community.domains.identifiers import BoardId
from app.community.domains.common import Level


@dataclass
class Board:
    id: BoardId
    name: str
    level: Level
