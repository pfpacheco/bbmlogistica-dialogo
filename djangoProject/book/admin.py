from django.contrib import admin
from book.models import Book


class BookInline(admin.StackedInline):

    model = Book
    can_delete = True
    verbose_name_plural = 'Books'

    fields = ('Title', 'Author', 'Description', 'Isbn', 'Price')
    list_display = ('Title', 'Author', 'Description', 'Isbn', 'Price')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
