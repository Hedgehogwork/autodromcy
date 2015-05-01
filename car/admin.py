# -*- coding: UTF-8 -*-
from django.contrib import admin
from car.models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_on', 'active')

admin.site.register(Car, CarAdmin)
