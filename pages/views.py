from django.shortcuts import render
from .models import *
from cars.models import Car

def home(requests):
	teams=Teams.objects.all()
	featured_cars =  Car.objects.order_by('-created_date').filter(is_featured=True)
	all_cars = Car.objects.order_by('-created_date')
	data = { 'teams':teams,
			'featured_cars':featured_cars,
			'all_cars':all_cars
	}
	return render(requests,'pages/home.html',data)


def about(requests):
	return render(requests,'pages/about.html')

def services(requests):
	return render(requests,'pages/services.html')

def contact(requests):
	return render(requests,'pages/contact.html')
