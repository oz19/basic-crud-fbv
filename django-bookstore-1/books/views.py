from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse

from books.models import Book
from books.forms import BookForm


def root(request):
    return redirect('books:index')

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

def get_book(request, isbn):
    try:
        book = Book.objects.get(isbn=isbn)
    except ObjectDoesNotExist:
        book = None

    context = {
        'description': {
            'title' : 'Book detail',
            'h1'    : 'Book detail',
        },
        'book'  : book,
    }

    return render(request, 'books/book-detail.html', context=context)


def add_book(request):
    context = {
        'description': {
            'title' : 'Add book',
            'h1'    : 'Add book',
        },
    }

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('books:get_book', isbn=book.isbn)

    else:
        form = BookForm()
        context['form'] = form
        return render(request, 'books/add-book.html', context=context)

def edit_book(request, isbn):
    context = {
        'description': {
            'title' : 'Edit book',
            'h1'    : 'Edit book',
        },
    }

    try:
        book = Book.objects.get(isbn=isbn)
    except ObjectDoesNotExist:
        book = None
        return render(request, 'books/edit-book.html', context=context)
        
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('books:get_book', isbn=book.isbn)

    else:
        form = BookForm(instance=book)
        context['form'] = form
        context['book'] = book
        return render(request, 'books/edit-book.html', context=context)

def delete_book(request, isbn):
    try:
        book = Book.objects.get(isbn=isbn)
    except ObjectDoesNotExist:
        book = None

    if book:
        book.delete()
    
    return redirect('books:index')
