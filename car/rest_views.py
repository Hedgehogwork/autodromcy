# -*- coding: UTF-8 -*-
import logging

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser

from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions

from car.serializers import CarSerializer
from car.models import Car


logger = logging.getLogger(__name__)


class AnonymousAuthentication(object):

    def authenticate(self, request):
        return (AnonymousUser, None)

    def authenticate_header(self, request):
        return 'empty'


class CarList(generics.ListAPIView):
    authentication_classes = (AnonymousAuthentication,)
    allowed_methods = ('GET',)
    serializer_class = CarSerializer
    paginate_by = 20
    model = Car
    queryset = Car.objects.all()
