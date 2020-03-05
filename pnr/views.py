from django.shortcuts import render
import requests
from . import scrapping3,scrapping4

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
    if request.method=='POST':
        source = request.POST.get('from_station')
        destination = request.POST.get('to_station')
        date = request.POST.get('date')
        date = date.split(' ')
        mon, day, yr = date[0],date[1][:-1], date[2]
        months = {
            'Jan':'01',
            'Feb':'02',
            'Mar':'03',
            'Apr':4,
            'May':5,
            'Jun':6,
            'Jul':7,
            'Aug':8,
            'Sep':9,

        }

        print()
        print()
        print()
        print()
        print()
        print()
        print()

        print([day,months[mon],yr])
        trains = scrapping4.get_trains_between_stn(source,destination,[day,months[mon],yr])
        print(trains)
        return render(request, 'home.html')
    return render(request, 'home.html')
