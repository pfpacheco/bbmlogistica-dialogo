from django.db import models


class Author(models.Model):

    def __init__(self):
        super(Author, self).__init__()
        __tablename__ = "author"

    id = models.BigIntegerField(name="Id", primary_key=True, auto_created=True)
    name = models.CharField(name="Name", null=False, editable=True, unique=True, max_length=200)
    forewords = models.CharField(name="Forewords", null=True, editable=True, max_length=1000)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

    def get_author(self):
        return dict({"id": self.id, "name": self.name, "forewords": self.forewords})