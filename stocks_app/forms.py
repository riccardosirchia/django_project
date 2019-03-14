from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['symbol', 'no_shares', 'purchase_price', 'current_value', 'purchase_date']
