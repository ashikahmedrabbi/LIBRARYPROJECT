from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book
from catagory.models import Catagory

def home(request, catagorys_slug = None):
    data=Book.objects.all()
    brands = Catagory.objects.all()
    if catagorys_slug is not None:
        brand = Catagory.objects.get(slug = catagorys_slug)
        data = Book.objects.filter(brand = brand)
    brands = Catagory.objects.all()
    return render(request, 'home.html',{'data': data, 'brands':  brands})
    