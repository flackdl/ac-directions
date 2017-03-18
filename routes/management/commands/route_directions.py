import os
import requests
from routes.models import Route
from django.core.management.base import BaseCommand, CommandError

#-122.42,37.78;-77.03,38.91?access_token=pk.eyJ1IjoiZmxhY2thdHRhY2siLCJhIjoiY2l6dGQ2MXp0MDBwMzJ3czM3NGU5NGRsMCJ9.5zKo4ZGEfJFG5ph6QlaDrA'
DIRECTIONS_URL='https://api.mapbox.com/directions/v5/mapbox/cycling/'


class Command(BaseCommand):
    help = 'Retrieves route directions'
    
    def get_directions(self, coords):
        # flip flop lat/lng because mapbox expects it that way
        print coords
        print Route.coords_lng_lat(coords)
        coords_joined = ';'.join(Route.coords_lng_lat(coords))
        url = '%s%s?access_token=%s' % (DIRECTIONS_URL, coords_joined, os.getenv('MAPBOX_ACCESS_TOKEN'))
        print url
        return requests.get(url) 
        
        
    def handle(self, *args, **options):
        routes = Route.objects.all()
        for route in routes:
            response = self.get_directions(route.coords[:24])
            if response.ok:
                print response.content 
            self.stdout.write(self.style.SUCCESS('Successfully retrieved directions for %s' % route))
            break