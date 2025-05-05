from django.urls import path
from books.views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete'),
    path('add/', BookCreateView.as_view(), name='create'),
]
