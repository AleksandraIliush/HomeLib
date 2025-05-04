from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Книга')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']