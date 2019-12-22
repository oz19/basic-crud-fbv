from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTests(TestCase):

    def setUp(self):
        '''Setup for testing database'''
        Book.objects.create(name='Long title testing book 1', isbn=1111)
        Book.objects.create(name='Testing book 2', isbn=2222)
        Book.objects.create(name='', isbn=3333)

    def test_get_book_name_length(self):
        '''Testing class method to get book name length'''
        book = Book.objects.get(isbn=1111)
        self.assertEqual(book.get_name_length(), 25)
        book = Book.objects.get(isbn=2222)
        self.assertEqual(book.get_name_length(), 14)
        book = Book.objects.get(isbn=3333)
        self.assertEqual(book.get_name_length(), 0)


class ViewsTests(TestCase):

    def setUp(self):
        '''Setup for testing database'''
        Book.objects.create(name='Long title testing book 1', isbn=1111)
        Book.objects.create(name='Testing book 2', isbn=2222)
        Book.objects.create(name='', isbn=3333)

    def test_all_books_url(self):
        '''Testing views: Get all books view'''
        response = self.client.get(reverse('books:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['description']['h1'], 'Book list' )
        self.assertEqual(response.context['description']['title'], 'Book list' )

    def test_add_book_url(self):
        '''Testing views: Add book view'''
        response = self.client.get(reverse('books:add_book'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['description']['h1'], 'Add book' )
        self.assertEqual(response.context['description']['title'], 'Add book' )

    def test_get_book_url(self):
        '''Testing views: Get book detail view'''
        response = self.client.get(reverse('books:get_book', kwargs={'isbn':1111} ))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['description']['h1'], 'Book detail' )
        self.assertEqual(response.context['description']['title'], 'Book detail' )
        
    def test_edit_book_url(self):
        '''Testing views: Edit book view'''
        response = self.client.get(reverse('books:edit_book', kwargs={'isbn':1111} ))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['description']['h1'], 'Edit book' )
        self.assertEqual(response.context['description']['title'], 'Edit book' )

    def test_delete_book_url(self):
        '''Testing views: Delete book view'''
        response = self.client.get(reverse('books:delete_book', kwargs={'isbn':1111} ))
        self.assertEqual(len(Book.objects.all()), 2)
