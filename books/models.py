from datetime import date

from django.db import models
from django.urls import reverse

from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Книга')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='author_set', verbose_name='Автор')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_data = models.DateField(default=date.today, verbose_name='Дата создания')
    start_reading_date = models.DateField(default=date.today, verbose_name='Дата начала чтения')
    finish_reading_date = models.DateField(default=date.today, verbose_name='Дата окончания чтения')
    is_read = models.BooleanField(default=False, verbose_name='Книга прочитана')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']
    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'pk':self.pk})