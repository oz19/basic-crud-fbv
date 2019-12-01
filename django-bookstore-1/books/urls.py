from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_books, name='index'),
    path('add', views.add_book, name='add_book'),
    path('edit', views.edit_book, name='edit_book'),
    path('delete', views.delete_book, name='delete_book'),
]
