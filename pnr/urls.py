from django.urls import path
from . import views


urlpatterns =[
	path('', views.home, name='home'),
	path('pnr-status', views.pnr_status, name="pnr_status"),
	path('train-between-station', views.train_between_station,name="train_between_station"),

]