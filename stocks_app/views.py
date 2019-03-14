from django.shortcuts import render
from .models import Investor, Stock
from .forms import StockForm
from django.http import HttpResponseRedirect
from django.urls import reverse



def index(request):
    stocks = Stock.objects.all()
    investor = Investor.objects.get(investorid=1)

    return render(request, 'index.html', {'stocks': stocks, 'investor':investor})

def stock_form(request):
    if request.method != 'POST':
        # no data submitted create blank form
        form = StockForm()
    else:
        # PSOT data submitted; process data
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    context = {'form' : form}
    return render(request, 'stock_form.html', context)

