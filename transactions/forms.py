from django import forms
from .models import Transaction
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
        ]

    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.pop('account') 
        super().__init__(*args, **kwargs)
        

    def save(self, commit=True):
        self.instance.user = self.user_id
        self.instance.balance_after_transaction = self.user_id.balance
        return super().save()
    
class DepositForm(TransactionForm):
    def clean_amount(self): # amount field ke filter korbo
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount') # user er fill up kora form theke amra amount field er value ke niye aslam, 50
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )

        return amount