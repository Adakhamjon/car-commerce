from django.shortcuts import render
from .models import *
from cars.models import Car

def home(requests):
	teams=Teams.objects.all()
	featured_cars =  Car.objects.order_by('-created_date').filter(is_featured=True)
	all_cars = Car.objects.order_by('-created_date')
	# search_fields = Car.objects.values('model','city','year','body_style')
	model_search = Car.objects.values_list('model',flat=True).distinct()
	city_search = Car.objects.values_list('city',flat=True).distinct()
	year_search = Car.objects.values_list('year',flat=True).distinct()
	body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
	data = { 'teams':teams,
			'featured_cars':featured_cars,
			'all_cars':all_cars,
			# 'search_fields':search_fields,
			'model_search':model_search,
			'city_search':city_search,
			'year_search':year_search,
			'body_style_search':body_style_search,
	}
	return render(requests,'pages/home.html',data)


def about(requests):
	return render(requests,'pages/about.html')

def services(requests):
	return render(requests,'pages/services.html')

def contact(requests):
	return render(requests,'pages/contact.html')
