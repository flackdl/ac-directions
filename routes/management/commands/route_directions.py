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
        print url
        return requests.get(url) 
        
        
    def handle(self, *args, **options):
        routes = Route.objects.all()
        for route in routes:
            self.stdout.write(self.style.NOTICE('route has %s waypoints' % len(route.coords)))
            
            # get/create directions record for this route
            directions = Directions.objects.filter(route=route)
            if directions.exists():
                directions = directions[0]
            else:
                directions = Directions(
                    route=route,
                )
                
            # build a running list of directions while iterating over chunks of waypoints
            route_directions = None
            has_waypoints = True
            waypoint_index = 0
            try:
                while(has_waypoints):
                    fetch_waypoints = route.coords[waypoint_index:waypoint_index + MAX_WAYPOINTS]
                    response = self.get_directions(fetch_waypoints)
                    if response.ok:
                        json = response.json()
                        # first saving of directions for this route
                        if not route_directions:
                            self.stdout.write(self.style.NOTICE('first route iteration'))
                            # use first route returned
                            route_directions = json['routes'][0]
                        else:
                            # append legs
                            route_directions['legs'] += json['routes'][0]['legs']
                                
                        waypoint_index += MAX_WAYPOINTS
                        has_waypoints = waypoint_index <= len(route.coords) - 1
                    else:
                        raise Exception('bad response %s' % e)
            except Exception as e:
                self.stdout.write(self.style.WARNING('Failed getting directions for %s so skipping route entirely (%s)' % (route, e)))
                continue
            
            directions.directions = route_directions
            directions.save()
            self.stdout.write(self.style.SUCCESS('Successfully retrieved directions for %s' % route))