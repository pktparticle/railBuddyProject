from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import home, pnr_status, train_between_station

class TestUrls(TestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func,home)
    
    def test_pnr_status_resolves(self):
        url = reverse('pnr_status')
        self.assertEquals(resolve(url).func,pnr_status)


    def test_train_between_station_resolves(self):
        url = reverse('train_between_station')
        self.assertEquals(resolve(url).func,train_between_station)

 
class TestViews(TestCase):
     
    def setUp(self):
        self.client =Client()
        self.home_url = reverse('home')
        self.pnr_status_url = reverse('pnr_status')
        self.train_between_station_url = reverse('train_between_station')

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code ,200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_pnr_status_GET(self):
        response = self.client.get(self.pnr_status_url)

        self.assertEquals(response.status_code ,200)
        self.assertTemplateUsed(response,'home.html')

    def test_train_between_station_GET(self):
        response = self.client.get(self.train_between_station_url)

        self.assertEquals(response.status_code ,200)
        self.assertTemplateUsed(response,'home.html')



