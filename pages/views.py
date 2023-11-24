from django.shortcuts import render

def home(requests):
	return render(requests,'pages/home.html')


def about(requests):
	return render(requests,'pages/about.html')

def services(requests):
	return render(requests,'pages/services.html')

def contact(requests):
	return render(requests,'pages/contact.html')
