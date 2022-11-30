from django.shortcuts import render
from library.models import Book, Genre
from django.shortcuts import render, get_object_or_404, redirect
from cart.forms import CartAddProductForm

# Create your views here.


def index(request, genre_slug=None):
    """Returns list of books"""
    genre = None
    genres = Genre.objects.all()
    books = Book.objects.filter(available=True)

    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = books.filter(genre=genre)
    cart_book_form = CartAddProductForm()
    return render(request, 'core/index.html', {'genre': genre,
                                               'genres': genres,
                                               'books': books,
                                               'cart_book_form': cart_book_form})


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')
