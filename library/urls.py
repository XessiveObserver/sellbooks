from django.urls import path
from . import views


app_name = 'library'
urlpatterns = [
    # Link to genre addition page
    path('add_genre/', views.add_genre, name='add_genre'),
    # Link to book addition page
    path('add_book/', views.add_book, name='add_book'),

    # Book edit link
    path('<int:book_id>/',
         views.edit_book, name='edit_book'),

    # Genre edit link
    path('edit_genre/<int:genre_id>/',
         views.edit_genre, name='edit_genre'),
    # book listing and details
    path('', views.book_list, name='book_list'),
    path('<slug:genre_slug>/', views.book_list,
         name='book_list_by_genre'),
    path('<int:id>/<slug:slug>/', views.book_detail,
         name='book_detail'),
]
