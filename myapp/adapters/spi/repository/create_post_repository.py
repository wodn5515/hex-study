from myapp.ports.spi.boards import FindBoardPort
from myapp.ports.spi.posts import SavePostPort
from myapp.domains.identifiers import BoardId
from myapp.domains.boards import Board
from myapp.domains.posts import Post
from myapp.adapters.spi.models.communities import BoardEntity, PostEntity
from myapp.adapters.spi.exceptions.communities import BoardNotFound


class CreatePostRepository(
    FindBoardPort,
    SavePostPort
):
    def find_board(self, board_id: BoardId) -> Board:
        board_entity = self._get_board_entity(board_id)
        return Board(id=board_entity.pk, name=board_entity.name, level=board_entity.level)

    def save_post(self, post: Post) -> Post:
        pass

    def _get_board_entity(self, board_id: BoardId) -> BoardEntity:
        try:
            board_entity = BoardEntity.objects.get(id=board_id)
        except BoardEntity.DoesNotExist:
            raise BoardNotFound()
        else:
            return board_entity
