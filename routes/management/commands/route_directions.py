import os
import requests
from urllib import urlencode
from routes.models import Route, Directions
from django.core.management.base import BaseCommand, CommandError

DIRECTIONS_URL='https://api.mapbox.com/directions/v5/mapbox/cycling/'
MAX_WAYPOINTS = 25


class Command(BaseCommand):
    help = 'Retrieves route directions'
    
    def get_directions(self, coords):
        # flip flop lat/lng because mapbox expects it that way
        coords_joined = ';'.join(Route.coords_lng_lat(coords))
        params = {
            'steps': 'true',
            'continue_straight': 'true',
            'access_token': os.getenv('MAPBOX_ACCESS_TOKEN'),
        }
        url = '%s%s?%s' % (DIRECTIONS_URL, coords_joined, urlencode(params))
        return requests.get(url) 
        
        
    def handle(self, *args, **options):
        routes = Route.objects.all()
        for route in routes:
            route_directions = []
            has_waypoints = True
            coord_index = 0
            try:
                while(has_waypoints):
                    response = self.get_directions(route.coords[coord_index:MAX_WAYPOINTS - 1])
                    if response.ok:
                        print response.content
                        directions = Directions(
                            route=route,
                            # TODO - append vs overwrite
                            directions=response.content, 
                        )
                        directions.save()
                        coord_index += MAX_WAYPOINTS
                        has_waypoints = coord_index >= len(route.coords)
                    else:
                        raise Exception
            except Exception as e:
                self.stdout.write(self.style.WARNING('Failed getting directions for %s so skipping route entirely' % route))
                continue
                
            self.stdout.write(self.style.SUCCESS('Successfully retrieved directions for %s' % route))
            break