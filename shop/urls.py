from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^catalog/$', views.BookListView.as_view(), name='book_list'),
    url(r'^book/(?P<pk>\d)$', views.BookDeatilView.as_view(), name='book_detail'),
    url(r'^author/(?P<pk>\d)$', views.AuthorListView.as_view(), name='author_list'),
    url(r'^category/(?P<pk>\d)$', views.CategoryListView.as_view(), name='category_list'),

    url(r'^cart/$', views.CartView.as_view(), name='cart'),
    url(r'^cart_add/$', views.add_to_cart, name='add_to_cart'),
    url(r'cart_remove/$', views.remove_from_card, name='remove_from_card')
]