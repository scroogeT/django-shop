from django.views.generic import ListView, DetailView
from shop.models import *


class BookListView(ListView):
    """
    Каталог статей
    """
    model = Book
    context_object_name = 'books'
    paginate_by = 10

    template_name = 'shop/book_list.html'


class AuthorListView(BookListView):
    """
    Выборка каталога по автору
    """
    def get_queryset(self):
        return Book.objects.filter(authors__pk=self.kwargs['pk'])


class CategoryListView(BookListView):
    """
    Выборка каталога по категории
    """
    def get_queryset(self):
        return Book.objects.filter(categories__pk=self.kwargs['pk'])


class BookDeatilView(DetailView):
    """
    Описание книги
    """
    model = Book
