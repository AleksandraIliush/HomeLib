from django.contrib import admin

from authors.models import Author

class AuthorAdmin(admin.ModelAdmin):
    class Meta:
        model = Author
    list_display = ('first_name', 'last_name', 'surname')

admin.site.register(Author, AuthorAdmin)
