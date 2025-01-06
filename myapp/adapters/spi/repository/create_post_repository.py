from myapp.ports.spi.boards import FindBoardPort
from myapp.ports.spi.posts import SavePostPort, FindAuthorPort
from myapp.domains.identifiers import BoardId, UserId
from myapp.domains.boards import Board
from myapp.domains.posts import Post, Author
from myapp.adapters.spi.models.communities import BoardEntity, PostEntity
from myapp.adapters.spi.models.users import UserEntity
from myapp.adapters.spi.exceptions.communities import BoardEntityNotFound, UserEntityNotFound


class CreatePostRepository(
    FindBoardPort,
    SavePostPort,
    FindAuthorPort
):
    def find_board(self, board_id: BoardId) -> Board:
        board_entity = self._get_board_entity(board_id)
        return Board(id=board_entity.pk, name=board_entity.name, level=board_entity.level)

    def save_post(self, post: Post) -> Post:
        post_entity = self._create_post(post)
        return self._post_entity_to_domain(post_entity)

    def find_author(self, user_id: UserId) -> Author:
        user_entity = self._get_user_entity(user_id)
        return Author(id=user_entity.pk, level=user_entity.author.level)

    def _get_board_entity(self, board_id: BoardId) -> BoardEntity:
        try:
            return BoardEntity.objects.get(id=board_id)
        except BoardEntity.DoesNotExist:
            raise BoardEntityNotFound()

    def _get_user_entity(self, user_id: UserId) -> UserEntity:
        try:
            return UserEntity.objects.select_related("author").get(id=user_id)
        except UserEntity.DoesNotExist:
            raise UserEntityNotFound()

    def _create_post(self, post: Post) -> PostEntity:
        post_entity = PostEntity(
            board=post.board_id,
            author=post.author_id,
            title=post.title,
            content=post.content
        )
        post_entity.save()
        return post_entity

    def _post_entity_to_domain(self, entity: PostEntity) -> Post:
        post = Post(
            id=entity.pk,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            title=entity.title,
            content=entity.content,
            author_id=entity.author.user_id,
            board_id=entity.board_id
        )
        return post
