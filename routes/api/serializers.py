from django.contrib.auth.models import User, Group
from routes.models import Route, Coord
from rest_framework import serializers


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'name',)


class CoordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coord
        fields = ('latitude', 'longitude')
        
        
class RouteDetailSerializer(RouteSerializer):
    coords = CoordSerializer(many=True, read_only=True)
    
    class Meta:
        model = Route
        fields = ('id', 'name', 'coords')