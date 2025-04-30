from django.shortcuts import render

from books.models import Book

__all__ = (
    'home',
)
def home(request):
    qs = Book.objects.all()
    context = {'objects_list': qs}
    return render(request, 'books/home.html', context)
