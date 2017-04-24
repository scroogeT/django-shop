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

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['title'] = u'Каталог'

        return context


class BookDeatilView(DetailView):
    """
    Описание книги
    """
    model = Book
