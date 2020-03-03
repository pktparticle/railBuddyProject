from django.shortcuts import render
import requests
from . import scrapping3

def home(request):
    return render(request, 'home.html')

def pnr_status(request):
    if request.method=='POST':
        pnr=request.POST.get('pnr')
        booked,current = scrapping3.get_pnr_status(pnr)
        context={
            'pnr':pnr,
            'booked':booked,
            'current':current
        }
        return render(request,'home.html',context)
    return render(request, 'home.html')

def train_between_station(request):
    return render(request, 'home.html')
