# In library_app/admin.py
from django.contrib import admin
from .models import Book, Review, borrow

admin.site.register(Book)

admin.site.register(Review)
admin.site.register(borrow)
