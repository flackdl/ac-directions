import os
import glob
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Import gps files'

    def handle(self, *args, **options):
        for filename in glob.glob('routes/kml/*.kml'):
            tree = etree.parse(filename)
            r = tree.xpath('LookAt')
        self.stdout.write(self.style.SUCCESS('Successfully imported'))