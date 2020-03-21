from django.shortcuts import render
from django.http import HttpResponse
from .models import book
from datetime import datetime

books_name = []
books_public_year = []
books_publisher_name = []
books_edition = []
library_books = []
all_data = book.objects.all()

for name in all_data:
    books_name.append(name.book_name + '<br>')

for year in all_data:
    books_public_year.append(year.public_year)

for pub_name in all_data:
    books_publisher_name.append(pub_name.publisher_name+ '<br>')

for editions in all_data:
    books_edition.append(editions.edition+ '<br>')

def book_name(request):
    return HttpResponse(''.join(sorted(books_name)))

def input_book(request):
    book_index = books_name.index("book")
    return HttpResponse(books_name[book_index], books_public_year[book_index], books_publisher_name[book_index], books_edition[book_index])

def all_books(request):
    obj_1 = book.objects.all()
    for i in obj_1:
        library_books.append(i.book_name + "-"   + i.publisher_name + "-" + i.edition + '<br>')
    return  HttpResponse (''.join(library_books))

def books_by_date(request):
    sorted_list = []
    sorted_date = book.objects.all().order_by('-public_year')
    for object in sorted_date:
        sorted_list.append(str(object.public_year) + " -- " + object.book_name + " -- " + object.publisher_name + " -- " + object.edition + '<br>')
    return HttpResponse(sorted_list)
