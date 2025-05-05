from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Книга')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']
    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'pk':self.pk})