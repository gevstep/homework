from django.urls import path
from . import views

urlpatterns = [
    path('book_name', views.book_name),
    path('book', views.input_book),
    path('all_books', views.all_books),
    path('books_by_dates', views.books_by_date),
]
