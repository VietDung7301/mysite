from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre


def index(request):
    """View function for home page of site."""
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects. \
        filter(status__exact='a').count()

    num_authors = Author.objects.count()

    num_genres_search = Genre.objects.filter(
        name__icontains='comic').count()
    num_books_search = Book.objects.filter(
        title__icontains='ever').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_search': {
            'key': 'comic',
            'value': num_genres_search},
        'num_books_search': {
            'key': 'ever',
            'value': num_books_search}
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
