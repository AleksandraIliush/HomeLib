from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from books.forms import HtmlForm, BookForm
from books.models import Book

__all__ = (
    'home', 'BookDetailView',
)
def home(request, pk=None):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    # if pk:
    #     book = get_object_or_404(Book, id=pk)
    #     context = {'objects': book}
    #     return render(request, 'books/detail.html', context)
    form = BookForm()
    qs = Book.objects.all()
    context = {'objects_list': qs, 'form': form}
    return render(request, 'books/home.html', context)

class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = 'books/detail.html'