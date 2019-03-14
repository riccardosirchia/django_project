from django.contrib import admin
from .models import Stock, Investor

# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'no_shares', 'roi')

class InvestorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')

admin.site.register(Stock, StockAdmin)
admin.site.register(Investor, InvestorAdmin)