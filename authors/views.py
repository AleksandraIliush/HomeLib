from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

# from authors.forms import HtmlForm, AuthorForm
from authors.models import Author

__all__ = (
    'home', 'AuthorListView',
     'AuthorDetailView',
    # 'AuthorCreateView', 'AuthorUpdateView', 'AuthorDeleteView',

)
def home(request, pk=None):
    qs = Author.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'authors/home.html', context)

class AuthorListView(ListView):
    paginate_by = 2
    model = Author
    template_name = 'authors/home.html'


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()
    template_name = 'authors/detail.html'
#
# class AuthorCreateView(SuccessMessageMixin, CreateView):
#     model = Author
#     form_class = AuthorForm
#     template_name = 'authors/create.html'
#     success_url = reverse_lazy('authors:home')
#     success_message = "Книга успешно создана"
# class AuthorUpdateView(SuccessMessageMixin, UpdateView):
#     model = Author
#     form_class = AuthorForm
#     template_name = 'authors/update.html'
#     success_url = reverse_lazy('authors:home')
#     success_message = "Книга успешно отредактирована"
# class AuthorDeleteView(SuccessMessageMixin, DeleteView):
#     model = Author
#     template_name = 'authors/delete.html'
#     success_url = reverse_lazy('authors:home')
#     success_message = "Книга успешно удалена"
