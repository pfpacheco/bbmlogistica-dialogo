from django.contrib import admin
from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    fields = ('id', 'name', 'forewords')
    list_display = ('id', 'nome', 'forewords')
