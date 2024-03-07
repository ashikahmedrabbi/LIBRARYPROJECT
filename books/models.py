from django.db import models
from catagory.models import Catagory
from django.contrib.auth.models import User
from reglogin.models import UserAccount

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='books/media/uploads/')
    borrowing_price = models.DecimalField(max_digits=5, decimal_places=2)
    brand = models.ManyToManyField(Catagory)



    def __str__(self):
        return self.name
    
class Review(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='reviews')
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"reviews by {self.name}"
    

class borrow(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowing_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return f" borrowed {self.book.name}"
    