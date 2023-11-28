from django.shortcuts import render

def cars(requests):
	return render(requests,'cars/cars.html')
