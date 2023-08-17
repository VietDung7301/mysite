from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)


class BooksInline(admin.TabularInline):
    """This class used to defines format of inline book insertion."""
    model = Book
    extra = 0


class BooksInstanceInline(admin.TabularInline):
    """This class used to defines format of inline book-instance insertion."""
    model = BookInstance
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.

    Attributes:
        list_display: fields that will be displayed in list view
        fields: order of fields in detail view
        inlines: adds addition of books in author view
    """
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BooksInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models.

    Attributes:
        list_display: fields that will be displayed in list view
        inlines: adds addition of book instances in book view
    """
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Administration object for BookInstance models.

    Attributes:
        list_display: fields that will be displayed in list view
        list_filter: filters that will be displayed in sidebar
        fieldsets: groups of fields
    """
    list_display = ('book', 'status', 'due_back', 'id')

    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
