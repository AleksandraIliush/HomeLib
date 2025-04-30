from django.shortcuts import render, get_object_or_404

from books.models import Book

__all__ = (
    'home',
)
def home(request, pk=None):
    if pk:
        book = get_object_or_404(Book, id=pk)
        context = {'objects': book}
        return render(request, 'books/detail.html', context)
    qs = Book.objects.all()
    context = {'objects_list': qs}
    return render(request, 'books/home.html', context)
