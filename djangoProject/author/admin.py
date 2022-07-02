from django.contrib import admin
from author.models import Author


class AuthorInLine(admin.StackedInline):

    model = Author
    can_delete = True
    verbose_name_plural = "Authors"

    fields = ('Name', 'Forewords')
    list_display = ('Name', 'Forewords')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
