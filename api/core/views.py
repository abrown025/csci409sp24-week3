from django.db import models
from rest_framework import serializers
from django.shortcuts import render
from rest_framework import viewsets
from core.models import Airline, Airport, Runways, Flights
from core.serializers import Airline, Airport, Runways, Flights


# Create your views here.

class AirportViewSet(viewsets.ViewSet):

    queryset = Airport.objects.all()
    serializer = Airport

class AirlineViewSet(viewsets.ViewSet):

    queryset = Airline.objects.all()
    serializer = Airline

class RunwaysViewSet(viewsets.ViewSet):

    queryset = Runways.objects.all()
    serializer = Runways

class FlightsViewSet(viewsets.ViewSet):

    queryset = Flights.objects.all()
    serializer = Flights
