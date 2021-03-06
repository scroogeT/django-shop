# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Автор')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Заголовок')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('isbn', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='ISBN')),
                ('publisher', models.CharField(db_index=True, max_length=50, verbose_name='Издательство')),
                ('page_num', models.IntegerField(verbose_name='Количество страниц')),
                ('description', models.TextField(verbose_name='Описание')),
                ('in_stock', models.BooleanField(db_index=True, default=True, verbose_name='В наличии')),
                ('authors', models.ManyToManyField(to='shop.Author')),
            ],
            options={
                'ordering': ('title', 'year'),
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Категория')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='shop.Category'),
        ),
    ]
