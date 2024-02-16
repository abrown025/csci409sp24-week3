from rest_framework import serializers
from core.models import Airline, Airport, Runways, Flights

class AirlineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airline
        fields = ['airport', 'runway_number', 'length', 'width']
        read_only_fields = ['id']

class RunwaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Runways
        fields = ['aiport', 'runway_number', 'runway_designation', 'length', 'width']
        read_only_fields = ['id']

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flights
        fields = ['origin', 'destination', 'airline', 'departure', 'arrival', 'flight_number', 'aircraft_type']
        read_only_fields = ['id']
