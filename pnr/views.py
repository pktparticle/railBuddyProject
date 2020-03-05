from django.shortcuts import render
import requests
from . import scrapping3, scrapping4


def home(request):
	return render(request, 'home.html')


def pnr_status(request):
	if request.method == 'POST':
		pnr = request.POST.get('pnr')
		booked, current = scrapping3.get_pnr_status(pnr)
		context = {
			'pnr': pnr,
			'booked': booked,
			'current': current
		}
		return render(request, 'home.html', context)
	return render(request, 'home.html')


def train_between_station(request):
    if request.method == 'POST':
        source = request.POST.get('from_station')
        destination = request.POST.get('to_station')
        date = request.POST.get('date')
        date = date.split(' ')
        mon, day, yr = date[0], date[1][:-1], date[2]
        months = {
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12,

        }
        source, destination, arr = scrapping4.get_trains_between_stn(source, destination, [day, months[mon], yr])

        trains = []
        for train in arr:
            trn_num = train['trn_no']
            trn_name = train['trn_name']
            src = train['source']
            dep_time = train['departure time']
            des = train['destination']
            arr_time = train['arrival time']
            duration = train['duration']
            class_=[]
            fare = []
            for cl in train['fares']:
                class_.append(cl['Class'])
                fare.append(cl['Price'])

            trains.append([trn_num, trn_name, src, dep_time, des, arr_time, duration, class_ , fare])

        context = {
                'trains': trains,
                'source': source,
                'destination': destination,
            }
        return render(request, 'home.html', context)
    return render(request, 'home.html')

