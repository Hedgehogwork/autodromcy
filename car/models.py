# -*- coding: UTF-8 -*-
from django.db import models


class Car(models.Model):
    engine = models.CharField(max_length=200, null=True, blank=True)
    power = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    color = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    detail = models.CharField(max_length=400, null=True, blank=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    gears = models.CharField(max_length=200, null=True, blank=True)
    year = models.CharField(max_length=200, null=True, blank=True)
    milage = models.CharField(max_length=200, null=True, blank=True)
    posted_on = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return '{0} {1}'.format(self.title, self.posted_on)
