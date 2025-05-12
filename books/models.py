from datetime import date

from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Книга')
    description = models.CharField(max_length=100, default='Описание книги', verbose_name='Описание')
    created_data = models.DateField(default=date.today, verbose_name='Дата создания')
    start_read = models.DateField(default=date.today, verbose_name='Дата начала чтения')
    finish_read = models.DateField(default=date.today, verbose_name='Дата окончания чтения')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']
    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'pk':self.pk})