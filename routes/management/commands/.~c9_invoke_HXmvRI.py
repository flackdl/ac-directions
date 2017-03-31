import os
import time
import requests
import traceback
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
            
            # get/create directions record for this route
            directions = Directions.objects.filter(route=route)
            if directions.exists():
                self.stdout.write(self.style.WARNING('route %s exists so skipping' % route))
                continue
            else:
                directions = Directions(
                    route=route,
                )
                
            self.stdout.write(self.style.WARNING('fetching route %s which has %s waypoints' % (route, len(route.coords))))
                
            # build a running list of directions while iterating over chunks of waypoints
            route_directions = None
            has_waypoints = True
            waypoint_index = 0
            try:
                while(has_waypoints):
                    time.sleep(1)
                    fetch_waypoints = route.coords[waypoint_index:waypoint_index + MAX_WAYPOINTS]
                    response = self.get_directions(fetch_waypoints)
                    if response.ok:
                        json = response.json()
                        # first saving of directions for this route
                        if not route_directions:
                            # use first route returned
                            route_directions = json['routes'][0]
                        else:
                            # append legs
                            if json.get('routes') and len(json['routes']):
                                route_directions['legs'] += json['routes'][0]['legs']
                            else:
                                print fetch_waypoints
                                print re
                                self.stdout.write(self.style.NOTICE('No route found for waypoints, skipping'))
                                
                        waypoint_index += MAX_WAYPOINTS
                        # make sure we have at least two waypoints left
                        has_waypoints = len(route.coords) - 1 - waypoint_index >= 2;
                    else:
                        raise Exception(response.content)
            except Exception as e:
                self.stdout.write(self.style.NOTICE('Failed getting directions for %s so deleting route directions (%s)' % (route, e)))
                # delete this directions record if it's already been saved
                if directions.pk:
                    directions.delete()
                print traceback.format_exc()
                # just quit entirely - we may be throttled
                break
            
            directions.directions = route_directions
            directions.save()
            self.stdout.write(self.style.SUCCESS('Successfully retrieved directions for %s' % route))