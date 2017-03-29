from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres import fields


class JSONFieldCustom(fields.JSONField):
   def db_type(self, connection):
        return 'json'



class Route(models.Model):
    name = models.CharField(max_length=60)
    coords = fields.ArrayField(models.CharField(max_length=255), default=list())
    
    @classmethod
    def coords_lng_lat(cls, coords):
        # reverses the joined coord strings to lng,lat (mapbox expects this)
        lng_lat_coords = []
        for coord in coords:
            lat_lng = coord.split(',') 
            lng_lat_coords.append('%s,%s' % (lat_lng[1], lat_lng[0]))
        return lng_lat_coords
        
    
    def __unicode__(self):
        return self.name
        
        
class Directions(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    directions = JSONFieldCustom()