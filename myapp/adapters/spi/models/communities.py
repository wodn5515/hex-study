from myapp.adapters.spi.models.abstracts import TimeStampedModel
from django.db import models


class Board(TimeStampedModel):
    name = models.TextField()
    level = models.IntegerField()

    class Meta:
        db_table = "boards"


class Post(TimeStampedModel):
    board = models.ForeignKey("myapp.Board", on_delete=models.PROTECT)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()

    class Meta:
        db_table = "posts"

