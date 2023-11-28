from django.contrib import admin
from django.utils.html import format_html
from .models import *

class carAdmin(admin.ModelAdmin):
	def thumbnail(self,object):
		return format_html('<img src="{}" width="40"  />'.format(object.car_photo.url))

	thumbnail.short_description="Car Image"

	list_display = ('id','thumbnail','car_title','color','model','year','price','fuel_type','body_style','is_featured')
	list_display_links=('id','car_title',)
	list_editable = ('is_featured',)
	search_fields= ('model','price','color','city','body_style')
	list_filter = ('city','model')
admin.site.register(Car,carAdmin)