from django.urls import path
from books.views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail')
]
