from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

from shop.models import *


def index(request):
    return render(request, 'shop/index.jinja')


def about(request):
    return render(request, 'shop/about.jinja')


class BookListView(ListView):
    """
    Каталог статей
    """
    model = Book
    context_object_name = 'books'
    paginate_by = 20

    template_name = 'shop/book_list.jinja'

    def get_context_data(self, **kwargs):
        c = super(BookListView, self).get_context_data(**kwargs)
        user = self.request.user
        return c


class AuthorListView(BookListView):
    """
    Выборка каталога по автору
    """

    #login_url = '/login/'
    #redirect_field_name = ''
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
    template_name = 'shop/book_detail.jinja'
