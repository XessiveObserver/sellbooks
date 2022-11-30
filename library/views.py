from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Book
from .forms import AddGenreForm, AddBookForm
from cart.forms import CartAddProductForm


def book_list(request, genre_slug=None):
    """Returns list of books"""
    genre = None
    genres = Genre.objects.all()
    books = Book.objects.filter(available=True)

    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = books.filter(genre=genre)
    cart_book_form = CartAddProductForm()
    return render(request, 'library/book/book_list.html', {'genre': genre,
                                                           'genres': genres,
                                                           'books': books,
                                                           'cart_book_form': cart_book_form})


def book_detail(request, id, slug):
    """Returns details of a published book"""
    book = get_object_or_404(Book,
                             id=id,
                             slug=slug,
                             available=True)
    cart_book_form = CartAddProductForm()
    return render(request, 'library/book/book_detail.html',
                  {'book': book,
                   'cart_book_form': cart_book_form})


@login_required
def add_genre(request):
    """Adds genre."""
    if request.method != 'POST':
        # No data submitted create a blank form
        form = AddGenreForm()
    else:
        # Psot data submitted; process form
        form = AddGenreForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('library:add_genre')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'library/add_genre.html', context)


@login_required
def add_book(request):
    """Adds book."""
    if request.method != 'POST':
        # No data submitted create a blank form
        form = AddBookForm()
    else:
        # Psot data submitted; process form
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library:add_book')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'library/add_book.html', context)


@login_required
def edit_book(request, book_id):
    """Edit an existing entry."""
    book = get_object_or_404(Book,
                             id=book_id)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = AddBookForm(instance=book)
    else:
        # POST data submitted; process data.
        form = AddBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('library:book_list')
    context = {'book': book, 'form': form}
    return render(request, 'library/edit_book.html', context)


@login_required
def edit_genre(request, genre_id):
    """Edit an existing entry."""
    genre = get_object_or_404(Genre,
                              id=genre_id)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = AddGenreForm(instance=genre)
    else:
        # POST data submitted; process data.
        form = AddGenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('/library/', genre_id=genre_id)
    context = {'genre': genre, 'form': form}
    return render(request, 'library/edit_genre.html', context)
