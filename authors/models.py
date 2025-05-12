from django.db import models

from books.models import Book


class Author(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Автор')
    birth_date = models.DateField(verbose_name='Дата рождения')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_set', verbose_name='Книга')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']