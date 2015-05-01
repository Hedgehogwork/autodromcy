# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse

from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = (
            'id',
            'engine',
            'power',
            'title',
            'color',
            'price',
            'detail',
            'contact',
            'gears',
            'year',
            'milage',
            'posted_on',
            'active'
        )
