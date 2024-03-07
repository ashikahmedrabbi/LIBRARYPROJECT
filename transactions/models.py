from django.db import models
from django.contrib.auth.models import User
from reglogin.models import UserAccount


class Transaction(models.Model):
    account = models.ForeignKey(UserAccount, related_name = 'transactions', on_delete = models.CASCADE , null = True)
    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
