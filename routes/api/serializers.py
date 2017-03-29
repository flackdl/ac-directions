from django.contrib.auth.models import User, Group
from routes.models import Route, Directions
from rest_framework import serializers


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'name',)
        
        
class RouteDetailSerializer(RouteSerializer):
    
    class Meta:
        model = Route
        fields = ('id', 'name', 'coords')
        

class DirectionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Directions
        fields = ('route', 'directions',)
