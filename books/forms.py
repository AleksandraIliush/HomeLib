from django import forms

from books.models import Book


class HtmlForm(forms.Form):
    title = forms.CharField(label='Книга')

class BookForm(forms.ModelForm):
    title = forms.CharField(label='Книга', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название книги'
    }))

    class Meta:
        model = Book
        fields = ('title' , )