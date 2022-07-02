from django.db import models
from author.models import Author


class Book(models.Model):

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(null=False, editable=True, max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(null=False, editable=True, max_length=1000)
    isbn = models.CharField(null=False, editable=True, max_length=13)
    price = models.FloatField(null=False, editable=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title

    def __repr__(self):
        return [self.id, self.title, self.description]

    def get_book(self):
        return {"id": self.id, "title": self.title,
                "author": self.author, "description": self.description, "isbn": self.isbn, "price": self.price}
