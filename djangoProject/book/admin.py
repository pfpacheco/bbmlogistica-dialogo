from django.contrib import admin
from book.models import Book


class BookInline(admin.StackedInline):

    model = Book
    can_delete = True
    verbose_name_plural = 'Books'

    fields = ('id', 'title', 'author', 'description', 'isbn', 'price')
    list_display = ('id', 'title', 'author', 'description', 'isbn', 'price')


class BookAdmin(admin.ModelAdmin):
    inlines = [
        BookInline
    ]

