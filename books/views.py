from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic import DetailView, View, ListView
from .models import Book, Review, borrow
from django.shortcuts import redirect,get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from reglogin.models import UserAccount
from django.contrib import messages
from .models import borrow
from transactions.views import send_email


class DetailBookView(LoginRequiredMixin,DetailView):
    model = models.Book
    pk_url_kwarg = 'id'
    template_name = 'bookdetails.html'

    def post(self, request, *args, **kwargs):
        reviews_form = forms.reviewsForm(data=request.POST)
        book = self.get_object()

        if reviews_form.is_valid():
            new_review = reviews_form.save(commit=False)
            new_review.book = book
            new_review.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object 
        reviews = book.reviews.all()
        reviews_form = forms.reviewsForm()

        UserAccount = self.request.user.account
        has_borrowed = models.borrow.objects.filter(user=UserAccount, book=book).exists()
        context['reviews'] = reviews

        context['reviews_form'] = reviews_form
        context['has_borrowed'] = has_borrowed

        return context

    def get_form(self):
        return self.form_class(data=self.request.POST or None)
    


        

class BorrowBookList(LoginRequiredMixin, ListView):
    model = borrow
    template_name = 'borrow.html'
    context_object_name= 'borrowed_books'

    def get_queryset(self):
        UserAccount = self.request.user.account
        queryset = UserAccount.transactions.all()
        queryset = borrow.objects.filter(user = UserAccount)
        return queryset
    
class buy_now(LoginRequiredMixin,View):
    def get(self,request,id, **kwargs):
        book = get_object_or_404(Book, id = id)
        user = self.request.user
        if user.account.balance > book.borrowing_price:
            user.account.balance -= book.borrowing_price
            messages.success(request, 'book borrowed successful')
            user.account.save(update_fields=['balance'])
            borrow.objects.create(
                book = book,
                user = request.user.account,
                borrowing_date=timezone.now(),
            )
            
            return redirect('home') 
        else:
            messages.error(request, 'Insufficient balance to borrow the book')
            send_email(user,book.borrowing_price, 'borrow', 'Book Borrow Message','transactions/email_template.html')
            return redirect('home')

class BookReturnView(LoginRequiredMixin, View):
    def get(self,request,id, **kwargs):
        book = get_object_or_404(Book, id=id)
        user = self.request.user
        user.account.balance += book.borrowing_price 
        messages.success(request, 'book return successful')
        user.account.save(update_fields=['balance'])
        borrow_instance = get_object_or_404(borrow, book__id=id, user=request.user.account)
        borrow_instance.delete()
        send_email(user,book.borrowing_price,book.name, 'return_book', 'Book Return Message','transactions/email_template.html')
        return redirect('home') 
    

        