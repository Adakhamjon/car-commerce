from django.urls import path
from .views import *
urlpatterns = [
path("",cars, name = 'cars'),
path("<int:id>",car_detail,name='car_detail'),
path("search",search,name='search')
]