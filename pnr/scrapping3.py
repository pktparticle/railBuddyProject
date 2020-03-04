import requests
from bs4 import BeautifulSoup

# pnr_number ='2108073501'
def get_pnr_status(pnr):
		pnr_number = pnr
		res = requests.get('http://www.railyatri.in/pnr-status/' + str(pnr_number))
		soup = BeautifulSoup(res.text, 'html.parser')
		booked_time_stats = []
		current_stats = []
		i=2

		while(1):
			temp_booked = soup.select('#status > div:nth-of-type('+str(i)+') > div:nth-of-type(1) > p')
			temp_current = soup.select('#status > div:nth-of-type('+str(i)+') > div:nth-of-type(2) > p')
			if(temp_booked != []):
				booked_time_stats.append(temp_booked[0].text.strip())
				current_stats.append(temp_current[0].text.strip())
				i+=1
			else:
				break

		# If pnr nummber is invalid
		if(booked_time_stats == []):
			return -1,-1

		# for i in range(len(booked_time_stats)):
		# 	print('Passenger '+str(i+1)+' Booking time status : ' + booked_time_stats[i] + ' and Current status: ' + current_stats[i])
		return booked_time_stats, current_stats
