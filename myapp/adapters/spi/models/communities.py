from myapp.adapters.spi.models.abstracts import TimeStampedModel
from django.db import models


class BoardEntity(TimeStampedModel):
    name = models.TextField()
    level = models.IntegerField()

    class Meta:
        db_table = "boards"


class PostEntity(TimeStampedModel):
    board = models.ForeignKey("myapp.BoardEntity", on_delete=models.PROTECT)
    author = models.ForeignKey("myapp.AuthorEntity", on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()

    class Meta:
        db_table = "posts"


class AuthorEntity(TimeStampedModel):
    user = models.OneToOneField("myapp.UserEntity", on_delete=models.PROTECT, related_name="author")
    level = models.PositiveIntegerField()
