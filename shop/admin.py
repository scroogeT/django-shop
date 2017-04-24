from django.contrib import admin
from shop import models


# TODO: Add separate search for publisher field
# TODO: Do something with authors viewing

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'publisher', 'in_stock', )
    list_filter = ('in_stock', )
    search_fields = ('title', )
    list_per_page = 50


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_per_page = 50


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_per_page = 50
