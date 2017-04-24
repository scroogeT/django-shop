from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^catalog/$', views.BookListView.as_view(), name='book_list'),
    url(r'^book/(?P<pk>\d)$', views.BookDeatilView.as_view(), name='book_detail'),
]