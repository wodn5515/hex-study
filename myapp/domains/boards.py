from dataclasses import dataclass
from myapp.domains.identifiers import BoardId
from myapp.domains.common import Level


@dataclass
class Board:
    id: BoardId
    name: str
    level: Level
