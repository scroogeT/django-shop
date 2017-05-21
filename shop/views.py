from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

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

    def get_queryset(self):
        return Book.objects.filter(in_stock=True)

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        return context


class AuthorListView(BookListView):
    """
    Выборка каталога по автору
    """

    def get_queryset(self):
        return Book.objects.filter(authors__pk=self.kwargs['pk'], in_stock=True)


class CategoryListView(BookListView):
    """
    Выборка каталога по категории
    """
    def get_queryset(self):
        return Book.objects.filter(categories__pk=self.kwargs['pk'], in_stock=True)


class BookDeatilView(DetailView):
    """
    Описание книги
    """
    model = Book
    template_name = 'shop/book_detail.jinja'


###############################################
# Views for shopping cart
###############################################

@login_required(login_url=reverse_lazy('shop:index'))
def add_to_cart(request):
    books = request.session.get('books', [])
    book_id = request.GET.get('book_id')

    if book_id not in books:
        books.append(book_id)
        request.session['books'] = books

        message = 'Книга успешно добавлена в корзину!'
    else:
        message = 'Ошибка: данная книга уже находится в корзине!'

    return render(request, 'shop/cart/cart_action.jinja', {'message': message})


@login_required(login_url=reverse_lazy('shop:index'))
def remove_from_card(request):
    books = request.session.get('books', [])
    book_id = request.GET.get('book_id')

    if book_id in books:
        books.remove(book_id)
        request.session['books'] = books

        message = 'Книга успешно удалена из корзины!'
    else:
        message = 'Ошибка: данной книги нет в корзине!'

    return render(request, 'shop/cart/cart_action.jinja', {'message': message})


class CartView(LoginRequiredMixin, BookListView):
    login_url = reverse_lazy('accounts:signin')
    template_name = 'shop/cart/cart.jinja'

    def get_queryset(self):
        if not 'books' in self.request.session:
            self.request.session['books'] = []

        return Book.objects.filter(id__in=self.request.session['books'])
