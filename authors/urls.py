from django.urls import path
from authors.views import *

urlpatterns = [
    #path('', home, name='home'),
    path('', AuthorListView.as_view(), name='home'),
    path('detail/<int:pk>/', AuthorDetailView.as_view(), name='detail'),
    # path('update/<int:pk>/', AuthorUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', AuthorDeleteView.as_view(), name='delete'),
    # path('add/', AuthorCreateView.as_view(), name='create'),
]
