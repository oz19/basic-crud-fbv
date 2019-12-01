from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book


def all_books(request):
    books   = Book.objects.all()
    context = {
        'description'   : {
            'title' : 'Book list',
            'h1'    : 'Book list',
        },
        'books'         : books,
    }
    
    return render(request, 'books/book-list.html', context=context)

def add_book(request):
    return HttpResponse('Add book page (under construction)')

def edit_book(request):
    return HttpResponse('Edit book page (under construction)')

def delete_book(request):
    return HttpResponse('Delete book page (under construction)')
