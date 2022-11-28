from django import forms

from .models import Genre, Book


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'slug']


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['genre', 'title', 'slug', 'image',
                  'description', 'price', 'available', 'created', 'updated', 'book']
