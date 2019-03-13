from django.shortcuts import render
from .models import Investor, Stock


def index(request):
    stocks = Stock.objects.all()
    investor = Investor.objects.get(investorid=1)

    return render(request, 'index.html', {'stocks': stocks, 'investor':investor})

