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

    def handle(self, *args, **options):
        # import all the kml routes
        for filename in glob.glob('routes/kml/*.kml'):
            tree = etree.parse(filename)
            tracks = tree.xpath('//gx:Tour//x:LookAt',
                namespaces=self.ns,
            )
            
            # create new route
            route = Route(name=filename)
            route.save()
            
            # assigne coordinates
            for track in tracks:
                Coord(
                    route=route,
                    longitude=track.xpath('./x:longitude', namespaces=self.ns)[0].text,
                    latitude=track.xpath('./x:latitude', namespaces=self.ns)[0].text,
                ).save()
                
        self.stdout.write(self.style.SUCCESS('Successfully imported'))