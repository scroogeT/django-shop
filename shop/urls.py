from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^catalog/$', views.BookListView.as_view(), name='book_list'),
    url(r'^book/(?P<pk>\d)$', views.BookDeatilView.as_view(), name='book_detail'),
    url(r'^author/(?P<pk>\d)$', views.AuthorListView.as_view(), name='author_list'),
    url(r'^category/(?P<pk>\d)$', views.CategoryListView.as_view(), name='category_list'),
]