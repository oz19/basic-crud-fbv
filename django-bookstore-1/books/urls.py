from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_books, name='index'),
    path('get/<int:isbn>', views.get_book, name='get_book'),
    path('add', views.add_book, name='add_book'),
    path('edit/<int:isbn>', views.edit_book, name='edit_book'),
    path('delete/<int:isbn>', views.delete_book, name='delete_book'),
]
