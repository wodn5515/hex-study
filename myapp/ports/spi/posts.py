from typing import Protocol
from myapp.domains.posts import Post, Author
from myapp.domains.identifiers import UserId


class SavePostPort(Protocol):
    def save_post(self, post: Post) -> Post:
        raise NotImplementedError()


class FindAuthorPort(Protocol):
    def find_author(self, author_id: UserId) -> Author:
        raise NotImplementedError()
