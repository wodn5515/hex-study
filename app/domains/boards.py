from dataclasses import dataclass
from app.domains.identifiers import BoardId
from app.domains.common import Level


@dataclass
class Board:
    id: BoardId
    name: str
    level: Level
