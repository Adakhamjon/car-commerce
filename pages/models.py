from django.db import models

class Teams(models.Model):
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	designation=models.CharField(max_length=200)
	photo=models.ImageField(upload_to='photos/%d/%m/%Y')
	facebook_link=models.URLField(max_length=100)
	twitter_link=models.URLField(max_length=100)
	google_plus=models.URLField(max_length=100)
	created_date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name
