from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from books.forms import HtmlForm, BookForm
from books.models import Book

__all__ = (
    'home', 'BookDetailView', 'BookCreateView', 'BookUpdateView', 'BookDeleteView'
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

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create.html'
    success_url = reverse_lazy('books:home')
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/update.html'
    success_url = reverse_lazy('books:home')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/delete.html'
    success_url = reverse_lazy('books:home')
