from django.contrib.auth.models import User, Group
from routes.models import Route, Coord
from rest_framework import serializers


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'name',)
        
        
class RouteDetailSerializer(RouteSerializer):
    coords = serializers.StringRelatedField(many=True)
    class Meta:
        model = Route
        fields = ('id', 'name', 'coords')


class CoordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coord
        fields = ('route', 'latitude', 'longitude')