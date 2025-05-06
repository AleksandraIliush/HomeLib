from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from books.forms import HtmlForm, BookForm
from books.models import Book

__all__ = (
    'home', 'BookDetailView', 'BookCreateView', 'BookUpdateView', 'BookDeleteView',
    'BookListView'
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
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
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

class BookListView(ListView):
    paginate_by = 2
    model = Book
    template_name = 'books/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = BookForm()
        context['form'] = form
        return context