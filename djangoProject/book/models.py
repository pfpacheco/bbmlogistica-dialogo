from django.db import models
from author.models import Author


class Book(models.Model):

    def __init__(self):
        super(Book, self).__init__()
        __tablename__ = "book"

    id = models.BigIntegerField(name="Id", primary_key=True, editable=False, auto_created=True)
    title = models.CharField(name="Title", null=False, editable=True, max_length=200)
    author = models.ForeignKey(Author, name="Author", on_delete=models.CASCADE)
    description = models.CharField(name="Description", null=False, editable=True, max_length=1000)
    isbn = models.BigIntegerField(name="isbn", null=False, editable=True)
    price = models.FloatField(name="price", null=False, editable=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    def __repr__(self):
        return [self.id, self.title, self.description]

    def get_book(self):
        return {"id": self.id, "title": self.title,
                "author": self.author, "description": self.description, "isbn": self.isbn, "price": self.price}
