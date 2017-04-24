from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(verbose_name=u'Автор', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = u'Автор'
        verbose_name_plural = u'Авторы'


class Category(models.Model):
    name = models.CharField(verbose_name=u'Категория', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class Book(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=200, db_index=True)
    year = models.IntegerField(verbose_name=u'Год', blank=True)
    isbn = models.CharField(verbose_name=u'ISBN', max_length=20, unique=True, db_index=True)

    publisher = models.CharField(verbose_name=u'Издательство', max_length=50, db_index=True, blank=True)
    page_num = models.IntegerField(verbose_name=u'Количество страниц', blank=True)
    description = models.TextField(verbose_name=u'Описание', blank=True)
    in_stock = models.BooleanField(verbose_name=u'В наличии', default=True, db_index=True)
    # photo = models.FileField(verbose_name=u'Фото', default=)

    authors = models.ManyToManyField(Author, blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', 'year', )
        verbose_name = u'Книга'
        verbose_name_plural = u'Книги'

    def get_absolute_url(self):
        return reverse('shop:book_detail', kwargs={'pk': self.id})
