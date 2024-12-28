from typing import Protocol
from app.domains.posts import Post


class SavePostPort(Protocol):
    def save_post(self, post: Post) -> Post:
        raise NotImplementedError()
