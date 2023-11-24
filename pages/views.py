from django.shortcuts import render
from .models import *

def home(requests):
	teams=Teams.objects.all()
	data = { 'teams':teams}
	return render(requests,'pages/home.html',data)


def about(requests):
	return render(requests,'pages/about.html')

def services(requests):
	return render(requests,'pages/services.html')

def contact(requests):
	return render(requests,'pages/contact.html')
