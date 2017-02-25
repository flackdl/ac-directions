import re
import os
import glob
from lxml import etree
from routes.models import Route, Coord
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Import gps files'
    ns = {
        'x': 'http://www.opengis.net/kml/2.2',
        'gx': 'http://www.google.com/kml/ext/2.2',
    }
    
    def get_route_name(self, filename):
        base = os.path.basename(filename)
        stripped = os.path.splitext(base)[0].replace('_', ' ')
        stripped = ' '.join([w.capitalize() for w in stripped.split(' ')])
        return re.sub(r' Route$', '', stripped)
        

    def handle(self, *args, **options):
        # import all the kml routes
        for filename in glob.glob('routes/kml/*.kml'):
            
            # build route name from file name
            route_name = self.get_route_name(filename)
            
            # existing route found so delete coords
            route = Route.objects.all().filter(name=route_name)
            if route:
                route = route[0]
                self.stdout.write(self.style.SUCCESS('Found existing route %s' % route_name))
                coords = Coord.objects.all().filter(route__id=route.id)
                self.stdout.write(self.style.SUCCESS('Deleting coords...'))
                coords.delete()
            # create new route
            else:
                self.stdout.write(self.style.SUCCESS('Importing new route %s' % route_name))
                route = Route(name=route_name)
                route.save()
            
            tree = etree.parse(filename)
            tracks = tree.xpath('//gx:Tour//x:LookAt',
                namespaces=self.ns,
            )
            
            # assign coordinates
            for track in tracks:
                Coord(
                    route=route,
                    longitude=track.xpath('./x:longitude', namespaces=self.ns)[0].text,
                    latitude=track.xpath('./x:latitude', namespaces=self.ns)[0].text,
                ).save()
                
        self.stdout.write(self.style.SUCCESS('Successfully imported'))