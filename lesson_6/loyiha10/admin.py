from django.contrib import admin
from .models import *
# Register your models here.


# class BooksAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'books_author', 'price', 'user_id']
# admin.site.register(Books)




admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
