from django.core.exceptions import ValidationError
from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Автор')
    first_name = models.CharField(max_length=100, default='', verbose_name='Имя')
    last_name = models.CharField(max_length=100,default='', verbose_name='Фамилия')
    surname = models.CharField(max_length=100,default='', verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.last_name}{self.first_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['last_name', 'first_name']

    def clean(self):
        qs = Author.objects.filter( first_name=self.first_name,
                                    last_name=self.last_name, surname=self.surname).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Такой автор уже есть в базе.")
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

