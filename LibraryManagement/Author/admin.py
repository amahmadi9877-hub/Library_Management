from django.contrib import admin
from Author.models import Author

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('published_books_count',)