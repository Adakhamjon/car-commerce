from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

class Car(models.Model):
	state_choice = (
		('AND','ANDIJAN'),
		('FER','FERGANA'),
		('NAM','NAMANGAN'),
		('TASH','TASHKENT'),
		('TASHv','TASHKENT VILOYATI'),
		('SAM','SAMARKAND'),
		('JIZ','JIZZAKH'),
		('BUKH','BUKHARA'),
		('SYR','SYRDARYA'),
		('QASH','QASHQADARYA'),
		('SUR','SURKHANDARYA'),
		('NAV','NAVOIY'),
		('KHO','KHORAZM'),
		)
	year_choice=[]
	for r in range(2000,(datetime.now().year+1)):
		year_choice.append((r,r))

	
	features_choice = (
		('Cruise Control','Cruise Control'),
		('Audio Interface','Audio Interface'),
		('Airbags','Airbags'),
		('Air Conditioning','Air Conditioning'),
		('Seat Heating','Seat Heating'),
		('Alarm System','Alarm System'),
		('ParkAssist','ParkAssist'),
		('Power Steering','Power Steering'),
		('Reversing Camera','Reversing Camera'),
		('Direct Fuel Injection','Direct Fuel Injection'),
		('Auto Start/Stop','Auto Start/Stop'),
		('Wind Deflector','Wind Deflector'),
		('Bluetooth Handset','Bluetooth Handset'),
		)

	doors_choice = (
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('6','6')
		)

	car_title=models.CharField(max_length=200)
	state=models.CharField(choices=state_choice,max_length=200)
	city=models.CharField(max_length=200)
	color=models.CharField(max_length=200)
	model=models.CharField(max_length=100)
	year=models.IntegerField(('year'),choices=year_choice)
	condition=models.CharField(max_length=100)
	price=models.IntegerField()
	description=RichTextField()
	car_photo = models.ImageField(upload_to='photos/%d/%m/%Y')
	car_photo_1=models.ImageField(upload_to='photos/%d/%m/%Y',blank=True)
	car_photo_2=models.ImageField(upload_to='photos/%d/%m/%Y',blank=True)
	car_photo_3=models.ImageField(upload_to='photos/%d/%m/%Y',blank=True)
	car_photo_4=models.ImageField(upload_to='photos/%d/%m/%Y',blank=True)
	features = MultiSelectField(choices = features_choice,max_length=300)
	body_style=models.CharField(max_length=100)
	interior=models.CharField(max_length=100)
	miles=models.IntegerField()
	doors=models.CharField(choices = doors_choice,max_length=10)
	passengers=models.IntegerField()
	vin_no=models.CharField(max_length=100)
	milage=models.IntegerField()
	fuel_type=models.CharField(max_length=100)
	no_of_owners=models.CharField(max_length=100)
	is_featured=models.BooleanField(default=False)
	created_date=models.DateTimeField(default=datetime.now(),blank=True)

	def __str__(self):
		return self.model

